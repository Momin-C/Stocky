<br />
  <p align="center">
  <a href="https://github.com/Momin-C/Stocky">
    <img src="images/Logo.png" alt="Logo" width="120" height="120">
  </a>
  <h3 align="center">Stocky</h3>
  <p align="center">
    Real-time Discord Stock Bot
    <br />
    <br />
    <a href="https://github.com/Momin-C/Stocky/issues">Report Bug</a>
  </p>
</p>

[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

## Table of Contents

* [About the Project](#about-the-project)
    * [Developed Using](#developed-using)
* [Demos](#demos)
* [Getting Started](#getting-started)
* [References](#references)
* [Contact](#contact)

## About The Project

Stocky allows you to view the price of stocks listed on US and Canadian Stock Exchanges in real-time. The bot gives daily graphs, info, daily numbers and more for any stock desired, all through simple easy-to-use commands!

### Developed Using
This project was developed using the Yahoo! Finance API and the Discord.py module.
* [Yahoo! Finance](https://pypi.org/project/yfinance/)
* [Discord.py](https://discordpy.readthedocs.io/en/stable/)

## Demos

GIFs of some commands can be found below.
Using the `$price` command

![](images/Price.gif)

Using the `$info` command

![](images/Info.gif)

Using the `$graph` command

![](images/Graph.gif)

## Getting Started

## Prerequisites
To use this bot, some packages need to be installed, download these packages from your terminal
```sh
pip3 install discord.py
pip3 install yfinance==0.1.62
pip3 install plotly
pip3 install kaleido
```
For best results when graphing, install the [Raleway](https://fonts.google.com/specimen/Raleway) font.

Then clone the repository

```sh
git clone https://github.com/Momin-C/Stocky.git
```

## Setting up the bot
Once the repository has been cloned, the bot must be activated using the discord developer portal. Either use the instructions written below or follow this [video](https://youtu.be/Uibz0iQjoC0?t=692) 


1. Go to the Discord developer portal [application website](https://discord.com/developers/applications)
2. Click New Application
3. Add a name for the application
4. Click the bot menu on the left and click "Add Bot"
5. Set the username to "Stocky" and use the logo in the images directory as the bot's picture
6. Go to the [bot permission website](https://discordapi.com/permissions.html) and select read messages, send messages, embed links and attach files
7. Under the permissions, paste the application ID which can be found on the "General Information" section of the discord developr portal
8. Click the link given and add the bot to your server
9. Right-click the "General" text channel and copy the channel ID, replace "842107220576567350" with this channel ID
10. On the discord developer portal bot site, copy the token and create a new file called ClientID.txt, paste this token there
11. Run the Stocky.py python file for the bot to be active

## References

* [Credit to othneildrew for the README template](https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md)
## Contact

Momin Chaudhry - [@momin_c](https://instagram.com/momin_c) - hellomomins@yahoo.com

Project Link: [https://github.com/Momin-C/Stocky](https://github.com/Momin-C/Stocky)

[issues-shield]: https://img.shields.io/github/issues/Momin-C/Stocky
[issues-url]: https://github.com/Momin-C/Stocky/issues
[license-shield]: https://img.shields.io/github/license/Momin-C/Stockye
[license-url]: https://github.com/Momin-C/Stocky/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/momin-chaudhry/