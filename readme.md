# Housie Ticker Generator

Creates unique housie(tambola) ticket based on username and date. Same username on same date will generate same board.


### Setup

Install the dependencies

    pipenv install

### Running Application
Run the flask application

    export FLASK_APP=app.py
    export LC_ALL=en_US
    flask run

Generate board by passing username to root url

http://127.0.0.1:5000/?username=username

### Result

<table border="1">
<tbody>
<tr><td style="padding: 10px;text-align: center;">&nbsp;&nbsp;&nbsp;</td><td style="padding: 10px;text-align: center;">11</td><td style="padding: 10px;text-align: center;">&nbsp;&nbsp;&nbsp;</td><td style="padding: 10px;text-align: center;">&nbsp;&nbsp;&nbsp;</td><td style="padding: 10px;text-align: center;">41</td><td style="padding: 10px;text-align: center;">54</td><td style="padding: 10px;text-align: center;">63</td><td style="padding: 10px;text-align: center;">&nbsp;&nbsp;&nbsp;</td><td style="padding: 10px;text-align: center;">81</td></tr>
<tr><td style="padding: 10px;text-align: center;">&nbsp;&nbsp;&nbsp;</td><td style="padding: 10px;text-align: center;">&nbsp;&nbsp;&nbsp;</td><td style="padding: 10px;text-align: center;">&nbsp;&nbsp;&nbsp;</td><td style="padding: 10px;text-align: center;">32</td><td style="padding: 10px;text-align: center;">45</td><td style="padding: 10px;text-align: center;">&nbsp;&nbsp;&nbsp;</td><td style="padding: 10px;text-align: center;">64</td><td style="padding: 10px;text-align: center;">77</td><td style="padding: 10px;text-align: center;">88</td></tr>
<tr><td style="padding: 10px;text-align: center;">2</td><td style="padding: 10px;text-align: center;">19</td><td style="padding: 10px;text-align: center;">&nbsp;&nbsp;&nbsp;</td><td style="padding: 10px;text-align: center;">&nbsp;&nbsp;&nbsp;</td><td style="padding: 10px;text-align: center;">&nbsp;&nbsp;&nbsp;</td><td style="padding: 10px;text-align: center;">56</td><td style="padding: 10px;text-align: center;">69</td><td style="padding: 10px;text-align: center;">80</td><td style="padding: 10px;text-align: center;">&nbsp;&nbsp;&nbsp;</td></tr>
</tbody>
</table>
