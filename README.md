# jamesmugford-talon

## Tab commands

`tabs.talon` provides global fallback commands. More-specific Community or
personal app contexts can override them.

| Command | Default shortcut |
| --- | --- |
| `tab open` / `tab new` | Ctrl+T |
| `tab next` | Ctrl+PageDown |
| `tab last` / `tab previous` | Ctrl+PageUp |
| `tab close` | Ctrl+W |
| `tab reopen` / `tab restore` | Ctrl+Shift+T |
| `go tab <number>` | Alt+number |
| `go tab final` | Alt+9 |
| `tab duplicate` / `tab clone` | Ctrl+L, then Alt+Enter |

Numbered-tab and duplicate shortcuts are browser-oriented defaults and depend
on the application supporting them. Community's tagged tab commands retain
their app-specific action implementations.

On Linux, `code/firefox_tabs.py` makes Firefox's next/previous actions select
adjacent tabs using Ctrl+PageDown/PageUp, regardless of its Ctrl+Tab preference.

## OBS recording

The `record mode` command enters `user.record`. While that mode is active,
`record toggle` toggles OBS recording and then plays a confirmation sound.
`command mode` and `mixed mode` leave record mode without changing OBS.

This integration requires:

- OBS Studio's authenticated WebSocket server on port 4455.
- `gobs-cli` configured to connect to `127.0.0.1`.
- Connection settings in `~/.config/gobs-cli/config.env`, outside this
  repository.
