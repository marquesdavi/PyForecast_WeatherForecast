<p><img src="./PyForecast%20art.jpg" style="width: 100vw; " align="middle"/></p>
<p>&nbsp;</p>
<h1 id="-description">☕ Description</h1>
<p><strong>PyForecast</strong> is a simple weather forecast application made in Python with the help of the pandas and requests library. The system has 4 main functions: </p>
<ul>
<li>[x] <mark style="background-color: #00FF00; border-radius: 3px; padding-left: 2px; padding-right: 2px">Date Forecast</mark> - It is a function that receives from the user a location and a date, and returns a table with the weather forecast for that specified date and location.</li>
<li>[x] <mark style="background-color: #00FF7F; border-radius: 3px; padding-left: 2px; padding-right: 2px">Period Forecast</mark> - It is a function that receives from the user a location, a start date and an end date, and returns a table with the weather forecast for that specified period.</li>
<li>[x] <mark style="background-color: #DC143C; border-radius: 3px; padding-left: 2px; padding-right: 2px">Perfect Weather</mark> - It is a function in which the user chooses a weather that he considers perfect and the system returns a table with the days when the weather will be in the condition informed.</li>
<li>[x] Create a <strong>.csv</strong> file that stores web requests in a table with index, acquisition date, target date, minimum and maximum temperature, location and weather condition.</li>
</ul>
<p>The system can show the weather forecast for several cities in Brazil.</p>
<p>&nbsp;</p>
<h1 id="-required-modules-and-languages-">📚 Required modules and languages:</h1>
<h2 id="used-language-">Used language:</h2>
<ul>
<li>Python 🐍<h2 id="modules-">Modules:</h2>
</li>
<li>pandas (<strong>pip install pandas</strong>)</li>
<li>requests (<strong>pip install requests</strong>)</li>
<li>termcolor (<strong>pip install termcolor</strong>)</li>
<li>unidecode (<strong>pip install unidecode</strong>)</li>
<li>os (This module is native to Python, but can be installed by using this command <strong>&quot;pip install os&quot;</strong>)</li>
</ul>
<p>The modules can also be installed using this command:</p>
<pre><code>pip <span class="hljs-keyword">install</span> requeriments.txt
</code></pre><p>&nbsp;</p>
<h1 id="-steps-taken-to-reach-this-result-">🎢 Steps taken to reach this result:</h1>
<ol>
<li>Requested the data with the HG Brasil API in JSON format.</li>
<li>Then I filtered the information and turned it into a DataFrame.</li>
<li>Export the dataframe to <strong>.csv</strong></li>
<li>Created the <mark style="background-color: #00FF00; border-radius: 3px; padding-left: 2px; padding-right: 2px">dateForecast( )</mark> function.  <ul>
<li>Returns a DataFrame with the weather forecast for a specific date.</li>
</ul>
</li>
<li>Created the <mark style="background-color: #00FF7F; border-radius: 3px; padding-left: 2px; padding-right: 2px">periodForecast( )</mark> function.<ul>
<li>Returns a DataFrame with the weather forecast between two different dates (MAX PERIOD: 10 days).</li>
</ul>
</li>
<li>Created the <mark style="background-color: #DC143C; border-radius: 3px; padding-left: 2px; padding-right: 2px">perfectWeather( )</mark> function.<ul>
<li>Returns a dataframe with the weather condition specified by the user.</li>
</ul>
</li>
<li>Created the Perfect Weather function menu.</li>
<li>Created the Main menu.</li>
</ol>
<p>&nbsp;</p>
<h1 id="-let-s-see-how-it-works-">🤖 Let&#39;s see how it works:</h1>
<p><br>
<img src="./pyforecast_photos/show_pyforecast.png" style="width: 100vw; " align="middle"/></p>
<p><br></p>
<h1 id="-observations-to-be-considered-">⚠️ Observations to be considered:</h1>
<ul>
<li>In the <mark style="background-color: #00FF7F; border-radius: 3px; padding-left: 2px; padding-right: 2px">periodForecast( )</mark> function, the the api only shows the forecast of a maximum of 10 days from the current date.</li>
<li>You can navigate the menus using the indexes for each feature.</li>
</ul>
<p>&nbsp;</p>
<h1 id="-license">📃 License</h1>
<h3 id="mit-license-dav-marques-https-github-com-marquesdavi-to-learn-more-check-the-license-file-by-clicking-here-license-md-">MIT License © <a href="https://github.com/marquesdavi">Daví Marques</a>. To learn more, check the license file by <a href="LICENSE.md">CLICKING HERE</a>.</h3>
