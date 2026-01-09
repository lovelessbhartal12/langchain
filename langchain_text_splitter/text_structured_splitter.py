from langchain_text_splitters import RecursiveCharacterTextSplitter

text=""" The economy of Nepal is primarily based on agriculture, which employs a large portion of the population. Major crops include rice, wheat, maize, and millet. Tourism is another key sector, contributing significantly to national income. Trekking, mountaineering, cultural tourism, and wildlife tourism attract visitors from around the world. Remittances sent by Nepali workers abroad also play a crucial role in the economy.

Despite its strengths, Nepal faces several challenges, including poverty, unemployment, political instability, and vulnerability to natural disasters such as earthquakes, floods, and landslides. However, the country has great potential for development through hydropower, tourism, education, and sustainable use of natural resources.

In conclusion, Nepal is a country of remarkable natural beauty, cultural richness, and historical importance. Although it faces development challenges, its diversity, resilience, and strategic location provide strong foundations for future progress."""


splitter=RecursiveCharacterTextSplitter(

    chunk_size=300,

    chunk_overlap=0
)

chunks=splitter.split_text(text)

print(len(chunks))

print(chunks)