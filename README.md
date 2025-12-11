# LLM-Assisted Marketing Insights Prototype

This project explores how large language models (LLMs) can support automated insight generation for marketing and campaign performance data. It is designed as a lightweight prototype demonstrating how AI can augment analytics workflows—summarising trends, identifying anomalies, and generating structured insights from complex metric sets.

The dataset used is a synthetic Adobe-Analytics-style campaign dataset that includes impressions, clicks, funnel steps, bounce rate, page load time, revenue, ROAS, and intentionally injected anomalies.  
The goal is to mimic realistic marketing analytics scenarios and test how LLMs behave when interpreting them.

---

## 🔍 **Project Objectives**

- Explore campaign and funnel performance across device, region, and channel segments  
- Detect meaningful shifts in metrics such as CTR, CVR, bounce rate, conversion rate, and ROAS  
- Prototype an LLM-powered insight generator capable of:
  - summarising performance changes
  - identifying anomalies
  - generating hypotheses grounded in the metrics provided
  - formatting output in structured text or JSON
- Test guardrails to keep the model focused on **metric-based reasoning**, not hallucinations  
- Establish a workflow that could evolve into a scalable insights tool

---

## 📊 **Dataset Overview**

The synthetic dataset (daily granularity, 10 campaigns) includes:

- **Campaign segmentation:** channel, device, region  
- **Core marketing metrics:** impressions, clicks, visits, spend, revenue  
- **Funnel steps:** landing → product view → add to cart → checkout → purchase  
- **Quality signals:** bounce rate, page load time  
- **Derived metrics:** CTR, CVR, ROAS  
- **Injected anomalies:**  
  - bounce + load time spike  
  - conversion rate drop  
  - inflated ROAS due to spend under-reporting

This allows testing how LLMs interpret noisy, realistic performance signals.

---

## 🧠 **LLM Prototype Goals**

`02_llm_insights.ipynb` demonstrates:

- Constructing a metric summary for a selected slice of data  
- Crafting prompts that:
  - emphasise evidence-based reasoning  
  - provide contextual guardrails  
  - limit hallucinations  
- Returning insights in either natural language or JSON  
- Highlighting meaningful patterns and potential root causes

Future improvements may include:
- Automated metric change detection  
- Batch insights for all campaigns/segments  
- Prompt evaluation framework  
- Integrating model confidence or uncertainty signalling  

---

## ⚙️ **How to Run the Project**

1. Clone the repository  
2. Open the project in VS Code  
3. Install the Python + Jupyter extensions  
4. Launch the notebooks and run cells interactively  
5. (Optional) Configure your OpenAI API key for LLM calls

---

## 📌 **Notes**

This is a prototype intended for exploration and learning.  
It is not a production system, but the architecture can grow into one with:

- scheduled data refresh  
- automated change detection  
- monitored LLM output quality  
- UI layer for marketers or internal users  

---

## 🙌 **Purpose**

This project serves as a learning exercise in:
- analytics prototyping  
- LLM-assisted insight methodologies  
- structuring early-stage DS/AI workflows  
- combining traditional metrics with generative capabilities  

It reflects modern expectations for analytical roles that partner closely with marketing, product, and engineering teams.
