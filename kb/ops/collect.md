# Collect

Collect liked posts from X (Twitter) or Reddit into `inbox/` using Playwright browser automation.

## Arguments

- **`x`** — Collect X (Twitter) likes
- **`reddit`** — Collect Reddit upvoted posts
- **No argument** — Ask the user which source to collect

## Prerequisites

- KB must be initialized (`index.md` must exist).
- Playwright MCP tools must be available.
- User must be logged in to the target platform in the browser session.

---

## Common: Deduplication

Before collecting, scan all existing files in `inbox/` for URLs. Build a set of known URLs.

1. Glob for `inbox/*.md` files.
2. Grep for URLs matching the platform pattern:
   - X: `https://x.com/`
   - Reddit: `https://www.reddit.com/r/`
3. Store these as the known URL set.

During collection, when a post's URL matches a known URL, **stop collecting**. Everything before that point is new.

---

## X (Twitter) Likes

### 1. Navigate to likes

The user's likes page is at `https://x.com/{username}/likes`. To find the username:

```
browser_navigate → https://x.com/likes
```

This will redirect to the logged-in user's profile. Check the page URL or sidebar profile link to extract the username, then navigate to `https://x.com/{username}/likes`.

Wait for the likes feed to load. Take a snapshot to confirm.

### 2. Collect posts by scroll-and-accumulate

X virtualizes the DOM — old tweets are removed as new ones load. You must extract data while scrolling.

Use `browser_evaluate` with the following scroll-and-accumulate script:

```javascript
() => {
  return new Promise(resolve => {
    const collected = new Map();
    // knownUrls should be injected as a Set of already-collected URLs
    const knownUrls = new Set([]); // ← inject dedup URLs here
    let stableRounds = 0;
    let lastSize = 0;
    let hitDuplicate = false;

    const interval = setInterval(() => {
      const articles = document.querySelectorAll('article');

      for (const article of articles) {
        const timeEl = article.querySelector('time');
        const dateLink = timeEl?.closest('a');
        const href = dateLink?.href || '';
        const statusMatch = href.match(/\/(\w+)\/status\/(\d+)/);
        if (!statusMatch) continue;

        const url = `https://x.com/${statusMatch[1]}/status/${statusMatch[2]}`;

        // Dedup check
        if (knownUrls.has(url)) {
          hitDuplicate = true;
          clearInterval(interval);
          resolve({ total: collected.size, tweets: Array.from(collected.values()), stopped: 'duplicate' });
          return;
        }

        if (collected.has(url)) continue;

        // Extract author — first @handle link only (avoid quoted tweet handles)
        const tweetContent = article.querySelector('[data-testid="tweetText"]')?.closest('[data-testid="tweet"]') || article;
        const authorLinks = article.querySelectorAll('a[href^="/"]');
        let author = '', handle = '';
        for (const link of authorLinks) {
          const h = link.getAttribute('href');
          if (h && h.match(/^\/\w+$/) && !h.includes('/status/')) {
            const t = link.textContent.trim();
            if (t.startsWith('@') && !handle) handle = t;
            else if (t && !author && t !== 'X') author = t;
          }
        }

        const textNodes = article.querySelectorAll('[data-testid="tweetText"]');
        const text = textNodes.length > 0 ? textNodes[0].textContent.trim() : '';

        const hasVideo = article.querySelector('[data-testid="videoPlayer"], [data-testid="videoComponent"]') !== null;
        const images = article.querySelectorAll('img[src*="pbs.twimg.com/media"]');
        const imageUrls = Array.from(images).map(img => img.src);

        collected.set(url, {
          author, handle, url,
          statusId: statusMatch[2],
          text,
          date: timeEl?.textContent || '',
          hasVideo,
          imageCount: imageUrls.length,
          imageUrls
        });
      }

      if (collected.size === lastSize) {
        stableRounds++;
        if (stableRounds >= 5) {
          clearInterval(interval);
          resolve({ total: collected.size, tweets: Array.from(collected.values()), stopped: 'end' });
        }
      } else {
        stableRounds = 0;
        lastSize = collected.size;
      }

      window.scrollBy(0, 800);
    }, 1500);

    setTimeout(() => {
      clearInterval(interval);
      resolve({ total: collected.size, tweets: Array.from(collected.values()), stopped: 'timeout' });
    }, 120000);
  });
}
```

Key details:
- `scrollBy(0, 800)` every 1.5 seconds
- Map keyed by tweet URL prevents duplicates within a session
- Stops when: known URL hit (dedup), 5 stable rounds (end of feed), or 2-minute timeout
- First `@handle` link only — avoids picking up quoted tweet handles

### 3. Collect notable replies

For each collected tweet, navigate to its URL and extract replies:

```javascript
// On the individual tweet page
() => {
  const replies = document.querySelectorAll('[data-testid="tweet"]');
  const result = [];
  let isFirst = true;
  for (const reply of replies) {
    if (isFirst) { isFirst = false; continue; } // skip the original tweet
    const author = reply.querySelector('a[href^="/"] [dir]')?.textContent || '';
    const handle = reply.querySelector('a[href^="/"] + div a')?.textContent || '';
    const text = reply.querySelector('[data-testid="tweetText"]')?.textContent || '';
    result.push({ author, handle, text: text.substring(0, 300) });
  }
  return result;
}
```

**Claude judges** which replies are notable. Keep replies that:
- Add useful context, data, or counterpoints
- Share relevant resources or tools
- Provide real-world experience or case studies
- Challenge the premise with evidence

Skip replies that are: simple agreement, jokes, self-promotion without substance, unrelated tangents.

### 4. Download media

#### Images

Download directly via curl. Image URLs from `pbs.twimg.com/media` are publicly accessible.

```bash
curl -L -o inbox/media/x-{statusId}-{index}.jpg "{imageUrl}"
```

Replace `name=small` or `name=medium` with `name=large` in the URL for best quality.

#### Videos / GIFs

X videos cannot be downloaded directly. Use savetwitter.net:

1. `browser_navigate` → `https://savetwitter.net/en4`
2. `browser_fill_form` → paste the tweet URL into the textbox (`textbox[name="Search"]`)
3. `browser_click` → the "Download" button
4. Wait for results to load, then `browser_evaluate` to extract download links:

```javascript
() => {
  const links = document.querySelectorAll('a');
  for (const link of links) {
    if (link.textContent.includes('Download MP4')) {
      return link.href; // first match = highest quality
    }
  }
  return null;
}
```

5. Download via curl:

```bash
curl -L -o inbox/media/x-{statusId}.mp4 "{downloadUrl}"
```

### 5. Write output file

Create `inbox/x-likes-YYYY-MM-DD.md`:

```markdown
# X(Twitter) 좋아요 수집

수집 시점: YYYY-MM-DD
수집 건수: N개

---

### 1. {tweet first line or summary}
- Author: @handle (Display Name)
- Date: YYYY-MM-DD
- URL: https://x.com/handle/status/id
- Media: ![](media/x-{statusId}-1.jpg) or [video](media/x-{statusId}.mp4)

{tweet full text}

#### Notable replies
- @reply_handle: {reply text}

---

### 2. {next tweet}
...
```

Order: newest first (as they appear in the likes feed).

---

## Reddit Upvoted

### 1. Navigate to upvoted

```
browser_navigate → https://www.reddit.com/user/me/upvoted/
```

This redirects to the logged-in user's upvoted page. Wait for the feed to load.

### 2. Collect posts by scroll-and-accumulate

Reddit uses `shreddit-post` custom elements with all metadata as attributes. No DOM virtualization.

```javascript
() => {
  return new Promise(resolve => {
    const collected = new Map();
    const knownUrls = new Set([]); // ← inject dedup URLs here
    let stableRounds = 0;
    let lastSize = 0;

    const interval = setInterval(() => {
      const posts = document.querySelectorAll('shreddit-post');

      for (const post of posts) {
        const permalink = post.getAttribute('permalink') || '';
        if (!permalink || collected.has(permalink)) continue;

        const url = 'https://www.reddit.com' + permalink;

        if (knownUrls.has(url)) {
          clearInterval(interval);
          resolve({ total: collected.size, posts: Array.from(collected.values()), stopped: 'duplicate' });
          return;
        }

        collected.set(permalink, {
          permalink,
          url,
          title: post.getAttribute('post-title') || '',
          author: post.getAttribute('author') || '',
          subreddit: post.getAttribute('subreddit-prefixed-name') || '',
          score: post.getAttribute('score') || '',
          commentCount: post.getAttribute('comment-count') || '',
          createdTimestamp: post.getAttribute('created-timestamp') || ''
        });
      }

      if (collected.size === lastSize) {
        stableRounds++;
        if (stableRounds >= 5) {
          clearInterval(interval);
          resolve({ total: collected.size, posts: Array.from(collected.values()), stopped: 'end' });
        }
      } else {
        stableRounds = 0;
        lastSize = collected.size;
      }

      window.scrollBy(0, 800);
    }, 1500);

    setTimeout(() => {
      clearInterval(interval);
      resolve({ total: collected.size, posts: Array.from(collected.values()), stopped: 'timeout' });
    }, 120000);
  });
}
```

### 3. Collect post body and notable comments

For each collected post, navigate to its URL and extract:

```javascript
() => {
  // Post body
  const postBody = document.querySelector('[slot="text-body"]');
  const bodyText = postBody ? postBody.textContent.trim() : '';

  // Top-level comments only (depth="0")
  const comments = document.querySelectorAll('shreddit-comment');
  const commentData = [];
  for (const comment of comments) {
    const depth = comment.getAttribute('depth') || '0';
    if (depth !== '0') continue;

    const author = comment.getAttribute('author') || '';
    const score = comment.getAttribute('score') || '';
    const textEl = comment.querySelector('[slot="comment"] p, [slot="comment"]');
    const text = textEl ? textEl.textContent.trim() : '';

    if (text) commentData.push({ author, score, text: text.substring(0, 500) });
  }

  // Media
  const images = document.querySelectorAll('[slot="post-media-container"] img');
  const imageUrls = Array.from(images).map(img => img.src).filter(src => src.includes('redd.it') || src.includes('imgur'));

  return { bodyText, comments: commentData, imageUrls };
}
```

**Claude judges** which comments are notable (same criteria as X replies).

### 4. Download media

#### Images

```bash
curl -L -o inbox/media/reddit-{postId}-{index}.jpg "{imageUrl}"
```

Extract `postId` from the permalink (the ID segment in `/comments/{postId}/`).

#### Videos

Reddit-hosted videos (`v.redd.it`) are difficult to download programmatically. Note the URL in the markdown for manual download:

```markdown
- Video: [v.redd.it link](https://v.redd.it/xxx) (manual download needed)
```

### 5. Write output file

Create `inbox/reddit-likes-YYYY-MM-DD.md`:

```markdown
# Reddit 좋아요 수집

수집 시점: YYYY-MM-DD
수집 건수: N개

---

### 1. {post title}
- Subreddit: r/{subreddit}
- Author: u/{author}
- Date: YYYY-MM-DD
- URL: https://www.reddit.com/r/...
- Score: {score}
- Media: ![](media/reddit-{postId}-1.jpg)

{post body text}

#### Notable comments
- u/{commenter} ({score}): {comment text}

---

### 2. {next post}
...
```

---

## After collection

Report to the user:
- How many posts were collected
- How many media files were downloaded
- How many were skipped (stopped at duplicate)

Suggest: "Run `/kb process inbox/{filename}.md` to create reference summaries."
