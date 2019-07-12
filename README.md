<h1><u> <center>Technical Analysis of National Stock Exchange</center> </u></h1>

<h2><u>Introduction</h2></u>
This project is an implementation of  automating the storage of NSE data into database

The purpose is to store the data in separate tables and to have a view of all the data conceretly which can further help the customers/users for easy understanding of prevalent market conditions.

To achieve the same, we have done evaluation on an interesting dataset and have analysed the obtained results.

A Database was created at first to store the data,python language was used as medium to communicate between 
the databases(MySQL) and (Python QT) the technology which was used to design UI.



<b>Limitations of NSE Website:</b> 
1) As the data available on NSE website is of csv format so we have to face certain problem like Accessing Anomalies , Inconsistency , Duplicate data So on this type of data we firstly converted it into the Table Data in Database.

2) And then we have daily download the data by visiting on website and then download and afterwards store into database we automated this process by just single click on button now you can download the file.

3) As the NSE Doesn't show that which share can be more profitable to buy I tried my best to predict it.


<b>Future Plan:</b>
1) To predict the stock more accurately by adding more number of parameters.
2) To predict GDP growth of India. 
3) To show different types of charts based on data available.




<h2><u><b> Versions</b> </u></h2>
 Python Version: 3.7
 DataBase: MySql Server 8.0

<h2><u><b> Setup:</b> </u></h2>
1) Design Preview Available
2) DataBase
3) Complete Python Setup
Avaliable Here: https://github.com/atharvaagrawal/analysis-of-national-stock-exchange/tree/master/PROCESS


<h2><u><b> Python File:</b> </u></h2>

<table>

<tr>
<td> FormDesign.py </td>
<td> Main File Contain Design and We can navigate to different scripts through this file. </td>
</tr>
    
<tr>
<td> CalculationUI.py </td>
<td> Calculation File Contain Design of Calculation and We can navigate to different scripts through this file. </td>
</tr>    

<tr>
<td>StoreDataIntoDataBaseNIFTY50.py</td>
<td>Script to Store Nifty50 DataBase. </td>
</tr>


<tr> 
<td>StoreBunchOfDataIntoNiftyAll.py</td>
<td>Script to Store All Data of One Folder to DataBase of BhavCopy. </td>
</tr>
    

<tr>
<td> StoreDataIntoDataBaseNIFTYALL.py</td> 
<td> Script for Nifty All BhavCopy DataBase Store. </td>
</tr>

<tr>
<td>NIFTY50FROMNIFTYALL.py</td>
<td> Copy only Top Nifty 50 Data from Nifty All DataBase. </td>
</tr>
    
<tr>
<td>DownloadDataFromWebNIFTY50.py</td>
<td> Download Nifty50 File From Web Automatically. </td>
</tr>

<tr>
<td>RemovePast200RecordsNIFTY50.py</td>
<td> Remove Past 200 days Record From Nifty50 </td>
</tr>


<tr> 
<td>CheckForRemainingDayNiftyAll.py</td>
<td>Script to Check from which date NiftyAll Data is Absent </td>
</tr>

<tr> 
<td>UpdateDataNiftyAllForRemainingDays.py</td>
<td>Script to Store Data in NiftyAll For Remaining Days </td>
</tr>

<tr>
<td> CalculatingLast5Days.py </td>
<td> Calculating Last 5 Days Record. </td>
</tr>    

</table>

<h2><u><b>Extra Files:</b> </u></h2>
<table>
<tr>
<td>geckodriver.exe:</td>
<td>In this geckodriver is for downloading data from web using selenium. Required for Mozilla Firefox.</td>
</tr>
<tr>
<td>logo.ico:</td> 
<td>Contain Logo</td>    
</tr>
</table>




<h2><u><b>Configue File: Config.cfg</b> </u></h2>

For Database:
1) host
2) database
3) user
4) password

For File Path:
1) store_bunch__nifty_all_path 
2) web_download_nifty50 
3) nifty_all_file_path 
4) nifty50_file_path
5) nifty_all_update_file_path


<h2><u><b> Directory Info: </b> </u></h2>
<table>

<tr>
<td>NIFTY50:</td>
<td>Contains Script related to Nifty50 </td>
</tr>

<tr>
<td>Data File:</td>
<td>Contains data file to store into database.</td>
</tr>

<tr>
<td>Config:</td>
<td>Contains Configure file </td>
</tr>

<tr>
<td>PROCESS:</td> 
<td>Contains structure of Project. </td>    
</tr>
</table>

