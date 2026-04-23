---
layout: page
title: Notes
description: >
  Short notes by David Beckwitt, imported from the ScatterGuy Substack RSS feed.
permalink: /notes/
image:
  path: /assets/img/social-card.jpg
  width: 1200
  height: 630
---

Short notes imported from [ScatterGuy](https://scatterguy.substack.com). The list refreshes from the Substack RSS feed when the website builds.
{:.lead}

[Read on Substack](https://scatterguy.substack.com){:.btn}
[RSS feed](https://scatterguy.substack.com/feed){:.btn}

{% assign substack_posts = site.data.substack_posts %}

{% if substack_posts and substack_posts.size > 0 %}
{% for post in substack_posts %}
## [{{ post.title | escape }}]({{ post.url }})

{{ post.published | date: "%B %-d, %Y" }}
{:.faded}

{{ post.summary | escape }}

[Read on Substack]({{ post.url }}){:.btn}
{% endfor %}
{% else %}
No Substack posts were available at the last site build. The latest posts are still available on [ScatterGuy](https://scatterguy.substack.com).
{% endif %}
