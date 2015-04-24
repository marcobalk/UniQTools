# UniQTools  [![Build Status](https://travis-ci.org/marcobalk/UniQTools.svg?branch=master)](https://travis-ci.org/marcobalk/UniQTools)

Package for some useful tools for Sublime Text

# TOC
<!-- MarkdownTOC -->

- [About UniQTools](#about-uniqtools)
- [Installation](#installation)
- [Active Commands](#active-commands)
- [Support](#support)
- [License](#license)

<!-- /MarkdownTOC -->


## About UniQTools
Package for some useful tools for Sublime Text

## Installation

To install UniQTools, Install Package Control First. See: <https://sublime.wbond.net/installation>

Then after restarting, run “Package Control: Add Repository” command, and enter [https://github.com/marcobalk/UniQTools][home] at the prompt.

Last but not least run “Package Control: Install Package” command, find and install `UniQTools` plugin.


## Active Commands

- PHP Serialize
- PHP Unserialze
- Alnum

### Alnum
With Alnum you can generate 25 character long code (default setting). Because of its length the generated code is always unique.
The first character is always a letter so it can be used as an identifier.
Works with multi-cursor; replaces your selection (if any).

#### Usage
- use `ctrl+A` (Mac) or `ctrl+3` (Windows/Linux) to generate an Alnum
- or open your context menu and go to 'UniQ Tools' -> 'Alnum'

#### Settings
```js
{
	"Alnum" : {
	  "length": 25, // minimum 1
	}
}
```

#### Examples
Some examples of generated codes:
```
jswohz0qui6k22bh2h9tlsp6v
rwwihh635gbaktr42pmt4tp10
zsh6diohtbh02z9mzgzuouthp
vmgrcpxgonz7578lld1mty9n2
mub7qhdixtbbh3ured2snlbo7
```

## Support

- Any bugs about UniQTools please feel free to report [here][issue].
- And you are welcome to fork and submit pullrequests.

## License

The code is available at github [project][home] under [MIT licence][1].

 [home]: https://github.com/marcobalk/UniQTools
 [issue]: https://github.com/marcobalk/UniQTools/issues
 [1]: https://github.com/marcobalk/UniQTools/blob/master/LICENSE
