import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

dataset=[

['A', 'B', 'C', 'D', 'F', 'H'],

['B', 'E', 'F', 'H'],

['A', 'C', 'E'],

['B', 'C', 'D', 'F', 'H'],

['A', 'B', 'C', 'D', 'E'],

['C','D','F','H'],

['A','C','D','H'],

['E','H']]

te=TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
print(df)
frequent_itemsets=apriori(df, min_support=0.5, use_colnames=True)

print(frequent_itemsets)
from mlxtend.frequent_patterns import association_rules
print(association_rules(frequent_itemsets, metric="confidence", min_threshold=0.75))
frequent_itemsets=apriori(df, min_support=0.6, use_colnames=True)
print(frequent_itemsets)
from mlxtend.frequent_patterns import association_rules
print(association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6))