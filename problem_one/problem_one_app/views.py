from django.shortcuts import render
import xlrd
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
	if request.method == 'POST':
		file = request.FILES['excel_file']
		fs = FileSystemStorage()
		filename = fs.save(file.name, file)
		uploaded_file_url = fs.url(filename)

		if file:
			xl_workbook = xlrd.open_workbook("media/%s" % file.name)
			sheet = xl_workbook.sheet_by_index(0)
			sheet.cell_value(5, 1)
			print(sheet.cell_value(4, 0))
			results = []
			for row in range(4, 7):
			    mid = (sheet.cell(row,0).value)
			    description  = (sheet.cell(row,0).value)
			    values  = (sheet.cell(row,1).value)
			    unit  = (sheet.cell(row,2).value)
			    print(unit)
			    details = {
			    	'description':description,
			    	'value':values,
			    	'unit':unit,
			    }
			    results.append(details)

		return render(request,'index.html',{ 'results': results })
	else:
		print('GET method part')
		return render(request,'index.html')