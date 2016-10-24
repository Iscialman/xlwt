#coding = utf-8
import  xlrd
import  xlwt
import  os
import  xlutils
from 	xlutils.copy import copy
import datetime

def get_data(para):
        if      para == 'charging':
                f               = open(r'D:\ribao\charingproc.txt')
                data_ep         = f.readlines()
                return data_ep

        
        elif    para == 'billing':
                f               = open(r'D:\ribao\billingproc.txt')
                data_hz        = f.readlines()
                return data_hz

        
        elif    para == 'remind':
                f               = open(r'D:\ribao\remind.txt')
                data_tx       = f.readlines()
                return data_tx
				
##				
##        elif    para == 'proc':
##                f               = open(r'D:\ribao\proc.txt')
##                data_proc       = f.readlines()
##                while data_proc :
##                        proc            = data_proc[:6]
##                        data_proc       = data_proc[6:]
##                        print data_proc
##                return proc
				
def get_index():
        wb 				= xlrd.open_workbook(r"D:\WX\dl_report\process_report.xlsx")
        sheet	        = wb.sheet_by_index(1)

        row_value       = sheet.row_values(0)

        for cont in row_value :
            today       = cont

        ##print row_value.index(today)

        col             = row_value.index(today)
        return col	
		
def write_excel():
		wb 		= xlrd.open_workbook(r"D:\WX\dl_report\process_report.xlsx")
		sheet	        = wb.sheet_by_index(1)
		max_col         = sheet.ncols

		newb            = copy(wb)

		for m in range(0,sheet.nrows) :
			for n in range(3,sheet.ncols ):
				old = sheet.cell(m,n)
				newb.get_sheet(1).write(m,n -1 ,old.value)
		
		f               = open(r'D:\ribao\proc_A.txt')
		data_proc       = f.readlines()

		erpi            = data_proc[0:7]
		hezhang         = data_proc[7:14]
		tixing          = data_proc[14:21]
		for data in erpi :
			newb.get_sheet(1).write(erpi.index(data)+1,max_col,data)
		for data in hezhang :
			newb.get_sheet(1).write(hezhang.index(data)+17,max_col,data)
		for data in tixing :
			newb.get_sheet(1).write(tixing.index(data)+33,max_col,data)		

		excel_name      = r"D:\ribao\proc_%s.xls" % datetime.date.today()
		newb.save(excel_name)
		
write_excel()
