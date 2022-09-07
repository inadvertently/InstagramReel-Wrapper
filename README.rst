.. image:: https://queensway.school/wp-content/uploads/2018/06/Instagram-Banner-Logo1.png
    :alt: InstagramReelWrapper

Instagram Reel Wrapper
--------

A lightweight, easy to use, asynchronus wrapper that extracts a reel from the url provided, converts it to an mp4, compresses the file to a smaller size, retrieves its bytes, and returns it.

Features
--------
- Asynchronus.
- No authentication needed.
- Optimised for quality yet decent speed.
--------


Basic Usage
--------
.. code:: py

    import asyncio, sys, os
    import instagram_reel as instagram
    
    async def do():
      url=input("URL: ")
      state, url, id = await instagram.check_url(url)
      if state:
         await instagram.download(url, id)
         print("Outputted")
      asyncio.run(do())
This example starts off by using the wrappers check function which attempts to validate the URL as a reel. If validated, we proceed to downloading it. The download function uses ``ytdl`` to download, then uses ``movie.py`` to decompress the outputted file **(not necessary).**

You can find another example using the lastest version of ``discord.py`` in the `examples directory <https://github.com/inadvertently/InstagramReelAPI/tree/main/IGReelAPI/InstagramReelAPI/examples>`_.
