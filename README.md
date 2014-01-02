# InfinitySVG-Mail: A Theme for Conky

## About

InfinitySVG-Mail is a theme for the "conky" system monitor for X. It is based on the InfinitySVG theme by Eric Weik.

![InfinitySVG-Mail screenshot](https://raw.github.com/PabloAng/ConkyInfinitySVG/master/images/InfinityMail-screenshot.png)


## Acknowledgements

As best I can tell, the following people had a hand in the creation of this theme.  Thank you!

- InfinirtySVG-Mail by: Pablo Angelani
- Original Conky Google Now:
	- [http://satya164.deviantart.com/art/Conky-Google-Now-366545753](http://satya164.deviantart.com/art/Conky-Google-Now-366545753)
- Original InfinitySVG by: Eric Weik
	- [http://www.newriversdigital.com/](http://www.newriversdigital.com/)
- Vector icons used in the background: "Iconic" by P.J. Onori
	- [http://somerandomdude.com/work/iconic/](http://somerandomdude.com/work/iconic/)
	- [https://github.com/somerandomdude/Iconic](https://github.com/somerandomdude/Iconic)
- Original Infinity theme by:	Harshit Yadav
	- [http://harshit1990.deviantart.com/art/Infinity-306921086](http://harshit1990.deviantart.com/art/Infinity-306921086)
- Includes lua code: Ring Meters by londonali1010 (2009)
	- [http://londonali1010.deviantart.com/](http://londonali1010.deviantart.com/)
	- [http://londonali1010.deviantart.com/gallery/#/d2ciqev](http://londonali1010.deviantart.com/gallery/#/d2ciqev)

## Installation Instructions

1. Install Conky
	- Ubuntu: apt-get install conky-all
	- Fedora: yum install conky
	- Other: see your local documentation or try [the Conky documentation](http://conky.sourceforge.net/documentation.html).
2. Extract the ConkyInfinitySVG distribution into its own directory somewhere.
	
3. Install Theme:
	- Automated Installation:
		- Execute ./setUp.sh: 
			- ~$ bash ./setUp.sh
		- Go to 8. 
	- Manual Installation:
		- Go to 4.
	
4. Copy .conkyrc, and .conky/ to your home directory:
	- ~$ cp .conkyrc ~/
	- ~$ cp -r .conky ~/

5. Open ~/.conkyrc in your favorite editor and adjust the screen resolution:
	- minimum_size 1920 1080

6. Replace in ~/.conkyrc:
	- 'YOUR EMAIL DOMAIN HERE' with your gmail username. Eg: myemail
	- 'YOUR OS' with your OS name: Eg: Ubuntu, Mint
	- 'YOUR OS VERSION' with your OS version. Eg: 13.04 (for Ubuntu), Cinnamon (for Mint)

7. Open ~/.conky/scripts/mail/userpwd.py and edit with your information:
	- Your can use base64 from any Linux terminal:
		- ~$ echo -n "myemail@gmail.com" | base64
		- ~$ echo -n "my pass" | base64

8. (optional) By default setup assumes we will set up Compiz manually for partial transparency of the conky output (step 9 below). If you are **not** using a compositing window-manager such as compiz, you can make the conky window transparent by altering the "own_window_type" and "own_window_transparent" settings in ~/.conkyrc.  Included in .conkyrc are three examples: manual with Compiz, automatic with a compositor, and automatic using conky directly.  Uncomment as desired if you wish to change this.

9. (optional) Check .conky/scripts/haunted.lua for any additional adjustments required for your screen resolution.

10. Now you are ready to run conky.  Open a terminal and run the following:
	- ~$ chmod a+x ~/.conky/startconky.sh
	- ~$ sh ~/.conky/startconky.sh
	- (Conky will start after 5 seconds.)

11. Add ~/.conky/startconky.sh as a startup application.
	- Ubuntu: Dash > (search) Startup Applications > Add
	- Other: see your location documentation to add this as a startup application.

12. We can use Compiz to make the conky window partially transparent.  This can be accomplished via ccsm - CompizConfig Settings Manager, use with caution (it is fairly easy to render your desktop unusable with ccsm).  If use set up conky to handle transparency in step 5, skip this step.
	- If not installed, install compizconfig-settings-manager 
	- Run ccsm
	- Go to: Accessibility > Opacity, Brightness and Saturation > (enable if not already)
	- In the Opacity tab, click "New"
	- In "Windows" enter "name=Conky" (exactly as shown -- do not just type "Conky")
	- In "Window values" enter "66" or so (higher for less transparent, lower for more)

13. Tweak the background image if you wish.
	- A vector based version of .conky/background.png is available for Inkscape in: images/background.svg
	- If you edit the svg, simply export the "page" at 90dpi and replace: .conky/background.png

14. Extras - Included in extras/terminator/config is a config file for the "Terminator" terminal program.  This sets up Terminator with a color scheme that matches this Conky theme.  To install it, back up your existing terminator configuration (~/.config/terminator/config) and copy in the one from extras/terminator/config.  ** If you have your own terminator config, you may wish to manually merge the title colors and profile colors from the supplied file into your own configuration.

15. Other notes:
	- The following scripts were written separately and currently are not used, but are included for example.
		- .conky/examples/cpu
		- .conky/examples/mail
		- .conky/examples/mem
		- .conky/examples/rings
		- .conky/examples/weather
		- .conky/examples/rings
	- For testing:  if you are testing changes to your background or the configuration files, you can skip using startconky.sh, and simply run conky directly.  In the distribution .conkyrc it is set to run in the background (via: background yes).  This means you'll need to run "killall conky;conky" to restart it.
	- A few random items in .conkyrc you might want to look at:
		- update_interval 5.0 (update interval in seconds)
		- default_color b7b7b7 (color of most of the text and graph outlines)
		- At the very bottom are a few examples of static text (a logo and multi-line text) that can be uncommented

