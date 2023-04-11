# Extra features in this theme

## Embed videos on Google Drive

You can **embed videos hosted in Google Drive** with this theme.

**Embed Google Drive videos** by uploading it to Google Drive, right-clicking it, click `Get link`, and click `🔗 Copy link`.
Paste the link into the `{video}` directive.
For example:

````
```{video} https://drive.google.com/file/d/1vtr54KvM7Vr01wZ1uz0bOrpDvnMGmKy8/view?usp=share_link
```
````

Results in:

```{video} https://drive.google.com/file/d/1vtr54KvM7Vr01wZ1uz0bOrpDvnMGmKy8/view?usp=share_link
```

**Embed youtube videos** by using the URL of the video you wish to embed (not the "share" link).
For example:

````
```{video} https://www.youtube.com/watch?v=lZ2FHTkyaMU&t=13s
```
````

Results in:

```{video} https://www.youtube.com/watch?v=lZ2FHTkyaMU&t=13s
```

## Header links

It adds a header that provides site-wide links across all of our documentation.

## CSS and visual style

We download the Mozilla Fira CSS and embed it in our side, since this is what our logo uses.

We also define several custom CSS rules to handle a header with cross-organization links.

## Redirect to `dirhtml`

2i2c's documentation uses the `dirhtml` builder so that pages exist at `pagename/index.html` instead of `pagename.html`.
However, the Sphinx default uses the `html` builder, and our documentation is often already built this way.
This theme includes a helper event callback that does two things:

- If `dirhtml` is the builder, create files to redirect `pagename.html` to `pagename/index.html`.
  This ensures that old `html` builder links redirect.
- If `html` is the builder, raise a warning that the `dirhtml` builder should be used instead.

## Extensions

**`sphinxext.opengraph`** adds OpenGraph tags to each of our sites.
It also pre-configures the social media cards to use `2i2c.org`.

**`sphinx-togglebutton`** allows us to make admonitions toggle-able with `:class: dropdown`.

**`sphinx-copybutton`** adds a copy button to each of our code blocks.
