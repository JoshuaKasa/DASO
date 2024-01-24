<h1 style="display: inline-block; vertical-align: middle;">DASO</h1>

**DASO is a simple tool for listening to music from YouTube directly from the terminal.**

<div align="center">
  <img src="img/porcodio_2.png" alt="Your Image Description">
</div>



## Installation

DASO comes with its own installer, a .bat file fow Windows which you can find in the main folder of the repository. Just run it and you're good to go. 

### By The Way

2 things:
1. For now there's no way of installing, running or using DASO on Linux or Mac. I'm NOT working on it and I don't plan to do it in the future.
2. There are 2 installers, [daso_installer_no_python.bat](daso_installer_no_python.bat) and [daso_installer_python.bat](daso_installer_python.bat). Funnily enough, the first one is for people who already have Python installed on their machine, the second one is for people who don't. If you don't know what Python is, just run the second one. In case the Python installer doesn't work, just install Python from [here](https://www.python.org/downloads/) and run the first installer.

## Usage

The DASO installer makes it so that you can run DASO from anywhere in your terminal. Basically, it adds a new command to your terminal, `daso`, which you can use to run like this:

```bash
daso [song name]
```

For example:

```bash
daso never gonna give you up
```

DASO uses the YouTube API to search for the song you want to listen to, so you can use any name you want, as long as it exists on YouTube. Remember tho, to provide a name, else you will get an error.

## Important

The neat thing about DASO is that it doesn't download the song you want to listen to, it just streams it from YouTube. Another important note is that you can't listen to Lives _for now_, I'm trying to figure out how to do it, if someone knows how to, you can [contribute](#contributing)!

## Contributing

If you want to contribute to DASO, you can do so by opening a pull request. I'm open to any kind of contribution, documentation, code, tests, suggestions, etc... Other than that, you can also open an issue if you find a bug or if you have a suggestion, I'll try to answer as soon as possible.

## License

[MIT](LICENSE)