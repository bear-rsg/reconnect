---
Authors: Talha Mansoor, Jack De Winter
Tags: unique
Date: 2019-07-03 19:56
Slug: add-tipue-search
Summary: Elegant can be configured to provide search for your static site, giving an alternate way to navigate the site.
Category: Advanced Features
---

Static sites usually do not offer search, as they are normally considered a dynamic task.
Elegant uses the open-source [Tipue Search](http://www.tipue.com/search/) plugin, to offer
search for your static site.

Here is an example of what the search result may look like:

![Search result for App Store]({static}/images/elegant-theme_search-result.png)

We have located the search box on the top right of the main navigation menu to allow
visitors to search from any page.

![Search box]({static}/images/elegant-theme_search-box.png)

To enable search, you need to enable the `tipue_search` plugin and add `search` to
`DIRECT_TEMPLATES` in your pelican configuration.

```python
PLUGINS = ['tipue_search']
DIRECT_TEMPLATES = ['search']
```

Note that these values must be added to any existing values present for the `PLUGINS` and
`DIRECT_TEMPLATES` configuration variables.
