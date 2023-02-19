# Tools

Some cool tools I use/to use


## Diagram as code

- Graphviz, dot
- plantUML
- MermaidJs

## Leaflet JS

Mobile friendly interactive Maps based on OpenStreetMap. Desktop+Mobile

## Create video of a terminal session

(This is just text so you can do CTRL+C & CTRL+V on the video) https://asciinema.org/
To embed the video in Markdown https://github.com/marionebl/svg-term-cli



## [GoTTY](https://github.com/yudai/gotty)

WebShell TTY

### Related

- [WebSSH](https://github.com/huashengdun/webssh): [digitalocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-connect-to-a-terminal-from-your-browser-using-python-webssh)


## [nip.io](https://nip.io/)

Dead simple wildcard DNS for any IP Address.
Stop editing your `/etc/hosts` file with custom hostname and IP address mappings.
nip.io allows you to do that by mapping any IP Address to a hostname using the following formats:

- Without a name:
  - 10.0.0.1.nip.io maps to 10.0.0.1
- With a name:
  - app.10.8.0.1.nip.io maps to 10.8.0.1

## [Asciinema](https://asciinema.org/)

Create video of a terminal, simple recording, copy & paste, embedding. This is just text so you can do `CTRL+C` & `CTRL+V` on the video.

### Recording a tmux session

```bash
tmux new -s terminal-capture # start a new session
<C-b> + d # detach from the session
asciinema rec -c "tmux attach -t terminal-capture" # record the tmux session
# do your stuff
<C-b> + d # detach from the session to stop recording
```

### Related

- [svg-term-cli](https://github.com/marionebl/svg-term-cli): Render asciicast to animated SVG
- [VHS](https://github.com/charmbracelet/vhs): Your CLI home video recorder vhs
- [peek](https://github.com/phw/peek): Simple animated GIF screen recorder with an easy to use interface.

## [Flameshot](https://github.com/flameshot-org/flameshot)

Powerful yet simple to use screenshot software.

## [borgbackup](https://doc.ubuntu-fr.org/borgbackup)

Extremely simple but powerful backup tool (with deduplication support)

