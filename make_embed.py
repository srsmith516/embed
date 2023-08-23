from langchain.embeddings import OpenAIEmbeddings

# Initialize the embeddings model
embeddings_model = OpenAIEmbeddings(openai_api_key="YOUR_OPENAI_API_KEY")

# Define the chunked text
text_chunk1 = """
Senate Bill No. 10
CHAPTER 163
An act to add Section 65913.5 to the Government Code, relating to land use.
[ Approved by Governor  September 16, 2021. Filed with Secretary of State  September 16, 2021. ]
LEGISLATIVE COUNSEL'S DIGEST
SB 10, Wiener. Planning and zoning: housing development: density.
The Planning and Zoning Law requires each county and city to adopt a comprehensive, long-term general plan for the physical development of the county or city and of any land outside its boundaries that bears relation to its planning. That law also requires the Department of Housing and Community Development to notify the legislative body of a city, county, or city and county whether the draft or amended housing element is in substantial compliance with specified provisions of that law. That law authorizes the department to review any action or failure to act by a city, county, or city and county that it determines is inconsistent with an adopted housing element or a specified provision of that law and to take specified actions to enforce that law.
Existing law, the Subdivision Map Act, vests the authority to regulate and control the design and improvement of subdivisions in the legislative body of a local agency, and sets forth procedures governing the local agency’s processing, approval, conditional approval or disapproval, and filing of tentative, final, and parcel maps, and the modification thereof.
This bill would authorize a local government to pass an ordinance to zone any parcel for up to 10 units of residential density per parcel, at a height specified by the local government in the ordinance, if the parcel is located in a transit-rich area, a jobs-rich area, or an urban infill site, as those terms are defined. In this regard, the bill would require the Department of Housing and Community Development, in consultation with the Office of Planning and Research, to determine jobs-rich areas and publish a map of those areas every 5 years, commencing January 1, 2022, based on specified criteria. The bill would specify that an ordinance adopted under these provisions is not a project for purposes of the California Environmental Quality Act. The bill would include findings that the changes proposed by this bill address a matter of statewide concern rather than a municipal affair and, therefore, apply to all cities, including charter cities.
By adding to the duties of local planning officials, this bill would impose a state-mandated local program.
The California Constitution requires the state to reimburse local agencies and school districts for certain costs mandated by the state. Statutory provisions establish procedures for making that reimbursement.
This bill would provide that no reimbursement is required by this act for a specified reason.
"""

# Embed the chunk
embedding1 = embeddings_model.embed_documents([text_chunk1])

print(embedding1)

text_chunk2 = """
Senate Bill No. 10
CHAPTER 163
An act to add Section 65913.5 to the Government Code, relating to land use.
[ Approved by Governor  September 16, 2021. Filed with Secretary of State  September 16, 2021. ]
THE PEOPLE OF THE STATE OF CALIFORNIA DO ENACT AS FOLLOWS:
SECTION 1. Section 65913.5 is added to the Government Code, to read:
65913.5. (a) (1) Notwithstanding any local restrictions on adopting zoning ordinances enacted by the jurisdiction that limit the legislative body’s ability to adopt zoning ordinances, including, subject to the requirements of paragraph (4) of subdivision (b), restrictions enacted by local initiative, a local government may adopt an ordinance to zone a parcel for up to 10 units of residential density per parcel, at a height specified by the local government in the ordinance, if the parcel is located in one of the following:
(A) A transit-rich area.
(B) A jobs-rich area.
(C) An urban infill site.
(2) A local government that adopts an ordinance pursuant to this section shall not limit the density of the parcel to less than 10 units of residential density per parcel.
(3) The creation of up to two accessory dwelling units and two junior accessory dwelling units per parcel pursuant to Sections 65852.2 and 65852.22 of the Government Code shall not count towards the total number of units of a residential or mixed-use residential project when determining if the project may be approved ministerially or by right under paragraph (1).
"""

# Embed the chunk
embedding2 = embeddings_model.embed_documents([text_chunk2])

print(embedding2)

text_chunk3 = """
Senate Bill No. 10
CHAPTER 163
An act to add Section 65913.5 to the Government Code, relating to land use.
[ Approved by Governor  September 16, 2021. Filed with Secretary of State  September 16, 2021. ]
(3) The creation of up to two accessory dwelling units and two junior accessory dwelling units per parcel pursuant to Sections 65852.2 and 65852.22 of the Government Code shall not count towards the total number of units of a residential or mixed-use residential project when determining if the project may be approved ministerially or by right under paragraph (1).
(4) A project may not be divided into smaller projects in order to exclude the project from the prohibition in this subdivision.
(d) (1) An ordinance adopted pursuant to this section shall not reduce the density of any parcel subject to the ordinance.
(2) A legislative body that adopts a zoning ordinance pursuant to this section shall not subsequently reduce the density of any parcel subject to the ordinance.
(e) For purposes of this section:
(1) “High-quality bus corridor” means a corridor with fixed route bus service that meets all of the following criteria:
(A) It has average service intervals of no more than 15 minutes during the three peak hours between 6 a.m. to 10 a.m., inclusive, and the three peak hours between 3 p.m. and 7 p.m., inclusive, on Monday through Friday.
(B) It has average service intervals of no more than 20 minutes during the hours of 6 a.m. to 10 p.m., inclusive, on Monday through Friday.
(C) It has average intervals of no more than 30 minutes during the hours of 8 a.m. to 10 p.m., inclusive, on Saturday and Sunday.
(2) “Transit-rich area” means a parcel within one-half mile of a major transit stop, as defined in Section 21064.3 of the Public Resources Code, or a parcel on a high-quality bus corridor.
(3) “Urban infill site” means a site that satisfies all of the following:
(A) A site that is a legal parcel or parcels located in a city if, and only if, the city boundaries include some portion of either an urbanized area or urban cluster, as designated by the United States Census Bureau, or, for unincorporated areas, a legal parcel or parcels wholly within the boundaries of an urbanized area or urban cluster, as designated by the United States Census Bureau.
(B) A site in which at least 75 percent of the perimeter of the site adjoins parcels that are developed with urban uses. For the purposes of this section, parcels that are only separated by a street or highway shall be considered to be adjoined.
(C) A site that is zoned for residential use or residential mixed-use development, or has a general plan designation that allows residential use or a mix of residential and nonresidential uses, with at least two-thirds of the square footage of the development designated for residential use.
(f) The Legislature finds and declares that provision of adequate housing, in light of the severe shortage of housing at all income levels in this state, is a matter of statewide concern and is not a municipal affair as that term is used in Section 5 of Article XI of the California Constitution. Therefore, this section applies to all cities, including charter cities.
"""

# Embed the chunk
embedding3 = embeddings_model.embed_documents([text_chunk3])

print(embedding3)

