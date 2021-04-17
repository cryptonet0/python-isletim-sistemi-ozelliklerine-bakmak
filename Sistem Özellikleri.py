# importing module 
import platform 

# dictionary 
info = {} 

# platform details 
platform_details = platform.platform() 

# adding it to dictionary 
info["İşletim Sistemi Detayları"] = platform_details 

# system name 
system_name = platform.system() 

# adding it to dictionary 
info["İşletim Sistem İsmi"] = system_name 

# processor name 
processor_name = platform.processor() 

# adding it to dictionary 
info["İşlemci Adı"] = processor_name 

# architectural detail 
architecture_details = platform.architecture() 

# adding it to dictionary 
info["Mimari Detayları"] = architecture_details

# printing the details 
for i, j in info.items(): 
	print(i, " - ", j) 
