import Water_contamination
 
InFolder = "c:\\igm\\projects\\Water_Contamination\\input\\"
OutFolder = "c:\\igm\\projects\\Water_Contamination\\output\\results\\"
QualityFile = "c:\\igm\\projects\\Water_Contamination\\Quality_Control.txt"
 
# List feature classes
FeatureReferenceList = References("High_Quality_Contamination_Data_R1.fatsq.gz", "High_Quality_Water_Contamination_Data_R2.fatsq2.gz", "reference_stats.txt")
 
# Loop through each feature class and clip
for FeatureReference in FeatureReferenceList:
     
    # Make the output path by concatenating strings
    OutputPath = OutFolder + FeatureReference
    # Clip the feature class
    Quality_Analysis(FeatureReference, QualityFile, OutputPath)

