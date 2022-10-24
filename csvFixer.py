import pandas as pd
mainImage = 'Dean_Road-Control-2_BW_LeftAngle'
url1 = 'Dean_Road-Control-2_BW_Sidewall'
url2 = 'Dean_Road-Control-2_BW_Tread'
df = pd.read_csv('RCTAS.csv')
df['productDescription'] = df['productDescription'] + '\n\n' + 'Features and Benefits' 
benefitCount = df['productFeaturesAndBenefitsParent'][0].count('{"S"')
for benefit in range(1, benefitCount + 1):
  df['productDescription'] = df['productDescription'] +'\n' + '- ' + df['productFeaturesAndBenefitsParent'][0].split('productFeaturesAndBenefits\":{\"S\":\"')[benefit]
df['productDescription'] = df['productDescription'].str.replace('"}}},{"M":{"', '')
df['productDescription'] = df['productDescription'].str.replace('"}}}]', '')
if 'uniformTireQualityGrade' not in df:
  df['uniformTireQualityGrade'] = ''
df = df[['websiteProductName','tireSize', 'loadIndexNumberSingle','speedSymbol','uniformTireQualityGrade','productId','aspectRatio','sectionWidthMm','wheelDiameter', 'productDescription']]
df = df.rename(columns={'websiteProductName' : 'Product', 'tireSize' : 'Size', 'loadIndexNumberSingle' : 'Load Index','speedSymbol' : 'Speed Rating','uniformTireQualityGrade' : 'UTQG','productId' : 'Sku','aspectRatio' : 'Tire Aspect Ratio','sectionWidthMm' : 'section-width','wheelDiameter' : 'Item Diameter', 'productDescription' : 'Product Description'})
df.insert(loc = 6, column = 'Price', value = '')
df.insert(loc = 7, column = 'Amazn Product Name', value = df['Product'] + ' ' + df['Size'])
df.insert(loc = 11, column = 'Main Image URL', value = f'https://www.lesschwab.com/dw/image/v2/BCDC_PRD/on/demandware.static/-/Sites-les-master-catalog/default/dw76e9fd44/images/ProductImages/{mainImage}.png')
df.insert(loc = 12, column = 'Other Image URL1', value = f'https://www.lesschwab.com/dw/image/v2/BCDC_PRD/on/demandware.static/-/Sites-les-master-catalog/default/dw76e9fd44/images/ProductImages/{url1}.png') 
df.insert(loc = 13, column = 'Other Image URL2', value = f'https://www.lesschwab.com/dw/image/v2/BCDC_PRD/on/demandware.static/-/Sites-les-master-catalog/default/dw76e9fd44/images/ProductImages/{url2}.png') 
df.insert(loc = 14, column = 'Swatch Image URL', value = df['Main Image URL'])  
df.insert(loc = 8, column = 'Item Type Keyword', value = 'automotive-light-truck-and-suv-all-terrain-tires')
# print(df['Product Description'])
df.to_csv('Amazon Tire List.csv', mode = 'a', index=False)

# import pandas as pd
# import os
# mainImage = 'Dean_Road-Control-2_BW_LeftAngle'
# url1 = 'Dean_Road-Control-2_BW_Sidewall'
# url2 = 'Dean_Road-Control-2_BW_Tread'
# directory = 'RC2'
# for filename in os.listdir(directory):
#   df = pd.read_csv(f'RC2/{filename}')
#   if 'productDescription' not in df:
#     df['productDescription'] = ''
#   if 'websiteProductName' not in df:
#     df['websiteProductName'] = 'Road Control 2'
#   df['productDescription'] = df['productDescription'] + '\n\n' + 'Features and Benefits' 
#   if 'productFeaturesAndBenefitsParent' not in df:
#     df['productFeaturesAndBenefitsParent'] = ''
#   benefitCount = df['productFeaturesAndBenefitsParent'][0].count('{"S"')
#   for benefit in range(1, benefitCount + 1):
#     df['productDescription'] = df['productDescription'] +'\n' + '- ' + df['productFeaturesAndBenefitsParent'][0].split('productFeaturesAndBenefits\":{\"S\":\"')[benefit]
#   df['productDescription'] = df['productDescription'].str.replace('"}}},{"M":{"', '')
#   df['productDescription'] = df['productDescription'].str.replace('"}}}]', '')
#   if 'uniformTireQualityGrade' not in df:
#     df['uniformTireQualityGrade'] = ''
#   df = df[['websiteProductName','tireSize', 'loadIndexNumberSingle','speedSymbol','uniformTireQualityGrade','productId','aspectRatio','sectionWidthMm','wheelDiameter', 'productDescription']]
#   df = df.rename(columns={'websiteProductName' : 'Product', 'tireSize' : 'Size', 'loadIndexNumberSingle' : 'Load Index','speedSymbol' : 'Speed Rating','uniformTireQualityGrade' : 'UTQG','productId' : 'Sku','aspectRatio' : 'Tire Aspect Ratio','sectionWidthMm' : 'section-width','wheelDiameter' : 'Item Diameter', 'productDescription' : 'Product Description'})
#   df.insert(loc = 6, column = 'Price', value = '')
#   df.insert(loc = 7, column = 'Amazn Product Name', value = df['Product'] + ' ' + df['Size'])
#   df.insert(loc = 11, column = 'Main Image URL', value = f'https://www.lesschwab.com/dw/image/v2/BCDC_PRD/on/demandware.static/-/Sites-les-master-catalog/default/dw76e9fd44/images/ProductImages/{mainImage}.png')
#   df.insert(loc = 12, column = 'Other Image URL1', value = f'https://www.lesschwab.com/dw/image/v2/BCDC_PRD/on/demandware.static/-/Sites-les-master-catalog/default/dw76e9fd44/images/ProductImages/{url1}.png') 
#   df.insert(loc = 13, column = 'Other Image URL2', value = f'https://www.lesschwab.com/dw/image/v2/BCDC_PRD/on/demandware.static/-/Sites-les-master-catalog/default/dw76e9fd44/images/ProductImages/{url2}.png') 
#   df.insert(loc = 14, column = 'Swatch Image URL', value = df['Main Image URL'])  
#   df.insert(loc = 8, column = 'Item Type Keyword', value = 'automotive-light-truck-and-suv-all-terrain-tires')
#   # print(df['Product Description'])
#   df.to_csv('RC2.csv', mode = 'a', index=False)