import os
import openai
from scipy.spatial import distance
import plotly.express as px
from sklearn.cluster import KMeans
from umap import UMAP

openai.api_key = "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 "


def get_embedding(text_to_embed):
	# Embed a line of text
	response = openai.Embedding.create(
    	model= "text-embedding-ada-002",
    	input=[text_to_embed]
	)
	# Extract the AI output embedding as a list of floats
	embedding = response["data"][0]["embedding"]
    
	return embedding

print(get_embedding("create view INFI_RnDAnalysis_SSAS_CSC2.V_ResultPlan_V1_IFCT0_G5_DemoSystem as SELECT [SourceSystem], [ScenarioDimId], [ProfitCenterDimId], [ProductHierarchyDimId], [LegalShareDimId], [CompanyCodeDimId], [CostCenterDimId], [WBSElementDimId], [JunkResultRnDDimId], [PostingYear], [PostingYearPeriodId], [PostingPeriodId], [TotalAmountCOAreaCurrency] *(1-(CAST([ProfitCenterDimId] as decimal)/10-FLOOR(CAST([ProfitCenterDimId] as decimal)/10) )/10 *5) * (1+(CAST([CompanyCodeDimId] as decimal)/10-FLOOR(CAST([CompanyCodeDimId] as decimal)/10) )/10 *3) as [TotalAmountCOAreaCurrency], [TotalAmountObjectCurrency] *(1-(CAST([ProfitCenterDimId] as decimal)/10-FLOOR(CAST([ProfitCenterDimId] as decimal)/10) )/10 *5) * (1+(CAST([CompanyCodeDimId] as decimal)/10-FLOOR(CAST([CompanyCodeDimId] as decimal)/10) )/10 *3) as [TotalAmountObjectCurrency] FROM [INFI_RnDAnalysis_SSAS_CSC2].[V_ResultPlan_V1_IFCT0_G5] fact --Select only projects from one company code INNER JOIN (SELECT ccdi_bs.DimensionId FROM [BUSV_FBI_OH_CSC1].[CompanyCodeDimensionID_BSATC_XX_X] ccdi_bs INNER JOIN [RAWV_RB_CSC1].[CompanyCode_WHUB0] cc_wh on cc_wh.CompanyCode_HK = ccdi_bs.CompanyCode_HK WHERE cc_wh.CompanyCode_BK LIKE ('9417') ) ccdi_bs_demo --RBOS-PS Company Code ON ccdi_bs_demo.DimensionId = fact.CompanyCodeDimId"))