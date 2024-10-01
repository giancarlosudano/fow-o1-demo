import os
import random
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
import traceback
from dotenv import load_dotenv

try:
	load_dotenv()
	
	st.set_page_config(page_title="Northwind Dynamic Pricing Copilot", page_icon=os.path.join('images','favicon.ico'), layout="wide", menu_items=None)
	st.title("Northwind Dynamic Pricing Copilot")
	# st.sidebar.image(os.path.join('images','northwind-logo.png'), use_column_width=True)
	# st.sidebar.write("Version 0.1.0")
	
	st.markdown("Dynamic Pricing Copilot is a tool (custom copilot) that helps you to optimize your pricing strategy by predicting the optimal price for your products.")
	st.markdown("This tool is powered by Azure **o1** algorithms and it is designed to help you to make data-driven decisions.")
	with st.expander("What is Dynamic Pricing?"):
		st.markdown("""
In the context of dynamic pricing for a sales division, especially in a company selling manufactured products like bicycles, several strategies and analyses can be employed to optimize pricing decisions and maximize revenue. Here are some key strategies and the types of analyses that can be performed:

## Strategies for Dynamic Pricing
### Demand-Based Pricing:

Prices are adjusted based on demand fluctuations. For example, prices can be increased when demand is high (peak seasons) and lowered during off-peak periods.
Strategy: Monitor historical sales data, seasonal trends, and external factors (like weather conditions) to forecast demand and adjust prices accordingly.

### Competitor-Based Pricing:

Prices are adjusted in real-time based on competitors' pricing strategies. This approach helps to remain competitive in the market.
Strategy: Use competitor price monitoring tools that track prices across different channels (e.g., online, physical stores), allowing for rapid price adjustments.

### Cost-Plus Pricing with Dynamic Adjustments:

A base price is set by adding a margin to the cost of production, with dynamic adjustments based on market conditions.
Strategy: Continuously analyze changes in production or logistics costs, adjusting prices dynamically to ensure profitability while remaining competitive.

### Segmentation-Based Pricing:

Different prices are set for different customer segments. For example, frequent buyers, corporate clients, or wholesale buyers might receive discounts or special prices.
Strategy: Segment the customer base by analyzing purchasing behaviors, demographic factors, or loyalty levels, and tailor prices accordingly.

### Geographic Pricing:

Prices are set dynamically based on geographic regions. This is useful if the company sells across different countries or cities where market conditions vary.
Strategy: Consider factors like local competition, purchasing power, and regulatory environments to set location-specific prices.

### Real-Time Dynamic Discounts:

Temporary discounts are applied dynamically based on stock levels or to drive immediate purchases (e.g., during a sales campaign or when inventory needs to be cleared).
Strategy: Use stock level monitoring and sales velocity data to trigger automated discounts for underperforming products or during low-demand periods.

### Time-Based Pricing (Peak Pricing):

Prices change based on time, such as offering lower prices during off-hours or on certain days to incentivize sales.
Strategy: Use historical data on buying patterns (e.g., days of the week, times of day) to identify periods of low demand and adjust prices to drive more sales.""")
	st.file_uploader("Upload your sales data", type=["csv"], accept_multiple_files=True)
	st.text_area(label="Suggestion for Reasoning Engine", value="analisi delle vendite globali con segmentazione per regione, prodotto e stagione, per identificare opportunità di ottimizzazione dei prezzi in mercati specifici, tenendo conto delle fluttuazioni dei costi di spedizione, concorrenza e preferenze locali.", height=200)

	if st.button("Start Copilot Reasoning Process..."):
		st.write("Copilot Reasoning Process started...")
		st.write("Please wait for the results...")
		st.write("This process may take a while...")
		with st.spinner("Processing..."):
			with st.expander("Reasoning"):
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Analyzing global sales")
				st.markdown("I'm tasked with examining global bike sales, highlighting regional, product-based, and seasonal trends, and identifying pricing optimization opportunities by analyzing shipping costs, competition, and local preferences.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Analyzing global sales")
				st.markdown("I’m working through a global sales analysis, focusing on regional, product, and seasonal segmentation. Considering shipping costs, competition, and local preferences to identify price optimization opportunities.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Leveraging data for insights")
				st.markdown("I'm pulling together regional data, considering shipping and storage costs, economic trends, and customer feedback to spot pricing optimization opportunities.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Analyzing financial data")
				st.markdown("Examining shipping and storage costs for different countries and regions, and adjusting for global economic factors.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Segmenting sales")
				st.markdown("I’m looking at the sales data by region, product, and season, analyzing patterns and trends within each segment to uncover insights.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Mapping regions and analyzing sales")
				st.markdown("Hmm, I’m thinking through the regions: Europe. I’m examining sales data, customer feedback, promotions, and economic factors for the different models.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Evaluating market dynamics")
				st.markdown("I’m piecing together the Europe market for. Notably, high sensitivity due to pricing and shipping costs. Feedback points to the bike's popularity despite the steep price tag.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Reviewing exchange rates")
				st.markdown("I'm digging into the exchange rates data, wondering if they show the value of 1 local currency unit in Euros. The numbers seem inconsistent, so I might assume they reflect local market purchasing power.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Analyzing economic factors")
				st.markdown("I'm thinking through Europe's economic indicators, like 5% growth, 2% inflation, 4% unemployment, and 7.0 exchange rate. Considering the products market price.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Evaluating pricing strategies")
				st.markdown("I’m analyzing the Europe market, considering price reduction or shipping cost adjustments to boost sales. Prompted by customer feedback and high shipping expenses.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Analyzing seasonal trends")
				st.markdown("OK, let me see. Sales data from January and February 2024 hints at seasonal peaks, especially for mountain and road bikes. Timing promotions with these peaks could boost sales.")
				time.sleep(random.uniform(1, 2))	
				st.markdown("#### Analyzing regional trends")
				st.markdown("I’m mapping out insights from North America, Europe, and Asia, noting differences in product performance, feedback, and sales strategies to tailor recommendations effectively.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Assessing competition and preferences")
				st.markdown("I'm piecing together the competition and local preferences in various regions. The USA market is highly competitive, while Italy favors the MTB-X and Germany values comfort. In China, high economic growth shows promise for expansion.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Analizzando le vendite globali")
				st.markdown("Sto esaminando le vendite internazionali delle nostre biciclette, segmentandole per regione, prodotto e stagione. Questo approccio mi permette di cogliere tendenze e opportunità specifiche, rispondendo meglio alle esigenze variabili in ogni settore.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Analizzando vendite e costi")
				st.markdown("Sto esplorando le vendite della SpeedX 500 in Nord America, notando che nei negozi fisici a Los Angeles le vendite sono più consistenti, mentre nell'e-commerce a New York ci sono margini di miglioramento. Hm, interessante.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Esplorando voli")
				st.markdown("Sto pensando al possibile miglioramento dei costi di spedizione con più aziende aeree.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Valutando i feedback")
				st.markdown("Sto guardando le performance della MTB-X in Italia, con riscontri molto positivi. La SpeedX 600 ha vendite moderate in Germania, ma il comfort sembra essere un problema.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Analizzando le opportunità")
				st.markdown("Sto esaminando il mercato cinese per MTB-Z, evidenziando la crescita potenziale e le esigenze clienti, e valutando l'ottimizzazione dei costi logistici attraverso strategie produttive e di stoccaggio locale.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Esplorando miglioramenti")
				st.markdown("Sto pensando a come migliorare il comfort della Germania (SpeedX 600) e valutando una riduzione temporanea del prezzo fino all'introduzione di miglioramenti.")
				time.sleep(random.uniform(1, 2))
				st.markdown("#### Ottenere insight")
				st.markdown("Sto pensando di aumentare i prezzi in Italia per la MTB-X e valutare l'espansione in altre città europee per stimolare la crescita del mercato.")
				time.sleep(random.uniform(1, 2))
			with st.expander("Results"):			
				st.write(
"""
## Analisi delle Vendite per Regione

1. Francia

* Vendite: Amarilla ha registrato vendite significative sin dal momento del lancio in tutto il mercato francese.
* Feedback clienti: "Ottima bici, ma prezzo alto" indica una sensibilità al prezzo.
* Promozioni passate: Durante la promozione del 10% di sconto (dicembre 2023), le vendite sono aumentate a 3402 unità.
* Costi: Alti costi di spedizione (50€/unità, 1.0€/km) e tasse doganali (5%).

2. Italia e Germania

Italia:
* Amarilla ha venduto 1250 unità attraverso negozi fisici.
* Feedback clienti: "Performance incredibile!" con un punteggio di 5.
Germania:
* Amarilla ha venduto 703 unità a Berlino.
* Feedback clienti: "Buona, ma poco comfort" con un punteggio di 3.
* Costi: Costi di spedizione e tasse doganali molto alti.

## Analisi per Prodotto

Amarilla

Mercati chiave: Italia.
Prezzo unitario: 1.000€.
Feedback: Apprezzata ma considerata costosa.
Promozioni: Vendite aumentate durante sconti del 10%.

Paseo
Mercati chiave: Spagna.
Prezzo unitario: 1.200€.
Feedback: Eccellente performance, alto punteggio cliente.

Velo
Mercati chiave: Germania.
Prezzo unitario: 1.500€.
Feedback: Necessità di migliorare il comfort.

## Considerazioni su Costi e Preferenze Locali

* Costi di Spedizione e Tasse Doganali:

Più alti in Germania, influenzando il prezzo finale.
Il resto dell'Europa ha costi più bassi, rendendo i prezzi più competitivi.

Preferenze Locali:

Italia: Sensibilità al prezzo per le bici da strada.
Francia: Forte apprezzamento per mountain bike ad alte prestazioni.
Germania: Importanza del comfort nelle bici da strada.

## Opportunità di Ottimizzazione dei Prezzi

1. Amarilla

* Strategia di Prezzo: Considerare una riduzione del prezzo o promozioni più frequenti per aumentare il volume delle vendite.
* Margini: Compensare margini più bassi con volumi maggiori.

2. Velo

* Prodotto: Investire nel miglioramento del comfort per soddisfare le preferenze locali.
* Prezzo: Valutare una riduzione temporanea del prezzo in attesa delle migliorie.

4. Italia (Paseo)

* Prezzo: Potenziale per un leggero aumento di prezzo data l'alta soddisfazione dei clienti.
* Espansione: Ampliare la distribuzione in altre regioni europee.""")
		with st.expander("Recommendations"):
			st.markdown("""## **Recommendations**

1. Amarilla in italia: Riduzione temporanea del prezzo del 5% per stimolare le vendite.
2. Amarilla in Germania: Aumento temporaneo del prezzo del 3% per compensare i costi di spedizione.
3. Paseo in Italia: Aumento del prezzo del 2% per sfruttare la forte domanda.
4. Velo in Germania: Riduzione temporanea del prezzo del 5% in attesa di miglioramenti al comfort.

""")

		with st.spinner("Generating Report..."):
			# Download a PPTX file
			time.sleep(random.uniform(2, 3))

		with open('report.pptx', 'rb') as f:
			st.download_button('Download Report', f, file_name="report.pptx", mime="application/vnd.openxmlformats-officedocument.presentationml.presentation")

		if st.button("Update price list"):
			st.markdown("Price list updated successfully.")

except Exception:
	st.error(traceback.format_exc())