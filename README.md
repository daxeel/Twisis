# Twisis 
Python module for twitter Analysis. <br>Twisis is combination of two words TWItter + analySIS <br>Twisis CLI support is coming soon.

# Dependencies
tweepy - Python client for Twiiter API
### Installing tweepy
```sh
sudo pip install tweepy
```
plotly - Pythn module for producing graphs
### Installing plotly
```sh
sudo pip install plotly
```

# Getting started
Let us analyze the positive sentimental of recent tweets regarding "programming" topic.
```py
import twisis
twisis_obj = twisis.Twisis('programming', 10)
response = twisis_obj.hashtag_analysis(plot=True, a_type='pos')
print response
```

Here, hashtag_analysis method has two parametersyou need to pass.<br><br>
<b>plot</b> : Tell twisis that if you want graph or not. <br>
<table>
	<tr>
		<td>True</td>
		<td>For plotting graph</td>
	</tr>
	<tr>
		<td>False</td>
		<td>Graph will not be generated. Only data will be provided</td>
	</tr>
</table>

<b>a_type</b> : Which type of analytics you want. There are 3 options.<br>
<table>
	<tr>
		<td>pos</td>
		<td>For positive sentimental analytics</td>
	</tr>
	<tr>
		<td>neg</td>
		<td>For negative sentimental analytics</td>
	</tr>
	<tr>
		<td>neu</td>
		<td>For neutral sentimental analytics</td>
	</tr>
</table>

Output will be this data
```json
[{
	"positive_number": 0.4510374202233184,
	"tweet": "#Programming https://t.co/shGN46Geyk",
	"negative_number": 0.5489625797766816,
	"neutral_number": 0.43492775762737645,
	"label": "neg"
}, {
	"positive_number": 0.5574349562599161,
	"tweet": "RT @tech_faq: How to Write Good Code. #programming #programmers #it #humor http://t.co/qlThMGy80P",
	"negative_number": 0.4425650437400839,
	"neutral_number": 0.16480314020649037,
	"label": "pos"
}, {
	"positive_number": 0.5310502542120531,
	"tweet": "8-year-old girl creates startup to teach kids to code: https://t.co/7m16JXlD8g @JanLeeThiem @CoderBunnyz #STEM #programming",
	"negative_number": 0.4689497457879469,
	"neutral_number": 0.9146021210199725,
	"label": "neutral"
}, {
	"positive_number": 0.4983975942854381,
	"tweet": "RT @javinpaul: Double Checked Locking on Singleton Class in Java https://t.co/n4S1n5DJy8 #Java #Programming https://t.co/EQggigfoOB",
	"negative_number": 0.5016024057145618,
	"neutral_number": 0.560905440868048,
	"label": "neutral"
}, {
	"positive_number": 0.5254729449991374,
	"tweet": "How to exchange data between a directive and controller in #AngularJS\nhttps://t.co/iX9qLRJpuA\n---\n#tutorial #JavaScript #dev #programming",
	"negative_number": 0.47452705500086256,
	"neutral_number": 0.7993149042951261,
	"label": "neutral"
}, {
	"positive_number": 0.8317505498266234,
	"tweet": "USB debugging on an S7 is great \ud83d\udc4dthe perfomance is amazing compared to the S5 #unity3d #SamsungGalaxyS7 #indiedev #gamedev #programming",
	"negative_number": 0.16824945017337656,
	"neutral_number": 0.22574509990218417,
	"label": "pos"
}, {
	"positive_number": 0.6237256953193774,
	"tweet": "RT @javacodegeeks: Download our #SpringData #Programming Cookbook for FREE! Join our #java newsletter https://t.co/02rdV6rnB4 https://t.co/\u2026",
	"negative_number": 0.3762743046806226,
	"neutral_number": 0.5771380351474564,
	"label": "neutral"
}, {
	"positive_number": 0.5805151353062492,
	"tweet": "Download our #SpringData #Programming Cookbook for FREE! Join our #java newsletter https://t.co/r75yJYfxGF https://t.co/aZFqQIgSQ9",
	"negative_number": 0.4194848646937508,
	"neutral_number": 0.5771380351474564,
	"label": "neutral"
}, {
	"positive_number": 0.5212050627444025,
	"tweet": "#Optimization of #code in #euler challenge #551 https://t.co/FD3t9VnSpk : an evolutionary tale\n#8thdev #programming #math #geek #algorithm",
	"negative_number": 0.4787949372555975,
	"neutral_number": 0.7932676882636737,
	"label": "neutral"
}, {
	"positive_number": 0.4115122132800094,
	"tweet": "CodeMill - a marketplace for pull requests #programming https://t.co/y3oNug6hGP https://t.co/sTFl3TxQCc",
	"negative_number": 0.5884877867199906,
	"neutral_number": 0.5700881564290919,
	"label": "neutral"
}]
```
And in your web browser this graph will be displayed.
<br>
<img src="https://raw.githubusercontent.com/daxeel/Twisis/master/sampleGraph.png"> 
