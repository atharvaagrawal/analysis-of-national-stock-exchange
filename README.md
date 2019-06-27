<h1><u> <center>Technical Analysis of National Stock Exchange</center> </u></h1>

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
<td>StoreDataIntoDataBaseNIFTY50.py</td>
<td>Script to Store Nifty50 DataBase. </td>
</tr>


<tr> 
<td>StoreBunchOfDataIntoNiftyAll.py</td>
<td>Script to Store All Data of One Folder to DataBase of BhavCopy. </td>
</tr>
    
<tr> 
<td>CheckForRemainingDayNiftyAll.py</td>
<td>Script to Check from which date NiftyAll Data is Absent </td>
</tr>

<tr> 
<td>UpdateDataNiftyAllForRemainingDays.py</td>
<td>Script to Store Data in NiftyAll For Remaining Days </td>
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
