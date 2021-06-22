<h1 style="text-align: center;">Welcome to DiveTools Gas Blending</h1>
<p style="text-align: center;"><span style="color: #ff0000;"><strong>This tool is for testing and educational use. &nbsp;</strong></span></p>
<p style="text-align: center;"><span style="color: #ff0000;">It is not intended to confirm the mix of breathing gases. &nbsp;If this tool is used a separate test is needed with an appropriate and calibrated and tested O2 and He sensor.</span></p>
<p>This tool will provide information for mixing Air, O2, and He with a SCUBA compressor. &nbsp;The intended use is to have two O2 sensors that are able to calculate a mix before it goes into a compressor. &nbsp;Two "Nitrox" sticks are used in series. &nbsp;One to mix in He and one to mix in O2.&nbsp; The tool can also be used as a nitrox analyser.</p>
<h2><strong>To Install this tool: </strong></h2>
<ul>
<li>Install latest Raspberry Pi OS with desktop.(2021-05-07-raspios-buster-armhf.img Tested)</li>
<li>Under Raspberry Pi Configuration --> Interfaces --> Enable "I2C"</li>
<li>pip install Adafruit_ADS1x15</li>
<li>apt-get install python3-tk</li>
<li>git clone git://github.com/divetools/Gas-Blending.git </li>
<li>ln -s ~/Gas-Blending/HEALTH.desktop ~/Desktop/HEALTH.desktop</li>
<li>Open File Manager --> Select Edit --> Preferences --> General Tick the option "Don't ask options on launch executable file"</li>
<p>Wire up an Adafruit ADS1115 to the pi I2C GPIOs. Connect two O2 sensors to port 0 and 1 on the ADS.</p>
<h2>Hardware Components:</h2>
<p>2021 Update - In an effort to reduce cost, I designed a new hardware case for the project.&nbsp; This case is 3D printed and will reduce the cost of the project.&nbsp; The STL's can be found at&nbsp;<a href="https://www.thingiverse.com/">https://www.thingiverse.com/</a>&nbsp;for download and printing.</p>
<table border="0" cellspacing="0" cellpadding="0"><colgroup><col width="292" /><col width="100" /><col width="87" /><col width="2047" /></colgroup>
<tbody>
<tr>
<th height="21">Part Name</th>
<th>QTY</th>
<th>Price</th>
<th>Link</th>
</tr>
<tr>
<td height="21">Raspberry Pi 3 B+ Motherboard</td>
<td>1</td>
<td>$55.96</td>
<td><a href="https://www.amazon.com/ELEMENT-Element14-Raspberry-Pi-Motherboard/dp/B07P4LSDYV/ref=sr_1_2_sspa?crid=2VBVS2OLMLLSQ&amp;keywords=raspberry+pi+3b%2B&amp;qid=1578837606&amp;sprefix=%2Caps%2C139&amp;sr=8-2-spons&amp;psc=1&amp;spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzOEpGNlEwRkVFT0dCJmVuY3J5cHRlZElkPUEwMTAwMzcxMkdFUVY3WEI4VFg4VCZlbmNyeXB0ZWRBZElkPUEwMDUxNzg2MVdRNUZaUkpYSEJOMSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=" target="_blank" rel="noopener">Amazon</a></td>
</tr>
<tr>
<td height="21">Raspberry Pi 3 Power Supply 5V 2.5A</td>
<td>1</td>
<td>$9.99</td>
<td><a href="https://www.amazon.com/Raspberry-Power-Supply-Adapter-Charger/dp/B0719SX3GC/ref=sr_1_6?crid=2ILU0YPQ4CIYB&amp;keywords=raspberry+pi+3b%2B+power+supply&amp;qid=1578837642&amp;sprefix=raspberry+pi+3b%2B+power%2Caps%2C134&amp;sr=8-6" target="_blank" rel="noopener">Amazon</a></td>
</tr>
<tr>
<td height="21">HiLetgo ADS1115 16 Bit</td>
<td>1</td>
<td>$6.99</td>
<td><a href="https://www.amazon.com/HiLetgo-Converter-Programmable-Amplifier-Development/dp/B01DLHKMO2/ref=sr_1_5?keywords=raspberry+pi+ADS&amp;qid=1578839525&amp;sr=8-5" target="_blank" rel="noopener">Amazon</a></td>
</tr>
<tr>
<td height="21">Micro SD Flash Drive</td>
<td>1</td>
<td>$13.89</td>
<td><a href="https://www.amazon.com/SanDisk-Extreme-microSDHC-UHS-I-SDSQXBG-032G-GN6MA/dp/B06XYDY93V/ref=pd_ybh_a_7?_encoding=UTF8&amp;psc=1&amp;refRID=19C291F42HYZ9ECZGNY7" target="_blank" rel="noopener">Amazon</a></td>
</tr>
<tr>
<td height="21">Raspberry Pi Official 7 Inch Touch Screen</td>
<td>1</td>
<td>$69.99</td>
<td><a href="https://www.amazon.com/Raspberry-Pi-Official-Touch-Screen/dp/B073S3LQ6Q/ref=sr_1_5?keywords=raspberry+pi+offical+touchscreen+7+inch&amp;qid=1578837882&amp;s=electronics&amp;sr=1-5" target="_blank" rel="noopener">Amazon</a></td>
</tr>
<tr>
<td height="21">3.5mm Stereo Jack</td>
<td>4</td>
<td>$3.20</td>
<td><a href="https://www.amazon.com/gp/product/B07BDBTRCD/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&amp;psc=1" target="_blank" rel="noopener">Amazon</a></td>
</tr>
<tr>
<td><strong>Total:</strong></td>
<td><strong>$160.02</strong></td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h2>Build Pictures:</h2>
<p><img src="https://github.com/divetools/Gas-Blending/blob/master/build_pictures/IMG_0324.jpeg?raw=true" width="610" height="418" /></p>
<p><img src="https://github.com/divetools/Gas-Blending/blob/master/build_pictures/IMG_0318.jpeg?raw=true" alt="" width="200" height="267" />&nbsp;<img src="https://github.com/divetools/Gas-Blending/blob/master/build_pictures/IMG_0319.jpeg?raw=true" alt="" width="200" height="267" />&nbsp;<img src="https://github.com/divetools/Gas-Blending/blob/master/build_pictures/IMG_0320.jpeg?raw=true" alt="" width="200" height="267" /></p>
<p><img src="https://github.com/divetools/Gas-Blending/blob/master/build_pictures/IMG_0321.jpeg?raw=true" alt="" width="200" height="129" />&nbsp;<img src="https://github.com/divetools/Gas-Blending/blob/master/build_pictures/IMG_0322.jpeg?raw=true" alt="" width="200" height="77" />&nbsp;<img src="https://github.com/divetools/Gas-Blending/blob/master/build_pictures/IMG_0323.jpeg?raw=true" alt="" width="200" height="212" /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
