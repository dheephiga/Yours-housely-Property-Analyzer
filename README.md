# Yours Housely🏡

A Property Analyzer aims to enable people to make the right decision about the property they choose to live in. This will also help people to check the compatibility of the house in which they wish to live with a `habitability score`.

The `habitability score` is calculated based on various factors including the water supply and the air quality index of the specified property. With the help of `machine learning`, the values of the attributes are analysed and the model is trained. Through this trained model one can choose the desired property to live in from the list of available properties

## Flowchart
```mermaid
graph LR
A[Feed dataset] --> C(Round Rect)
C[ML algorithm] --> D(Filter out data)
D[Filter out data] --> E(OUTPUT)
```
