from collections import Counter
txt = "The rapid advancements in technology have significantly transformed the way we live and work. From artificial intelligence to the Internet of Things, innovations have streamlined processes, improved efficiency, and connected people across the globe. For instance, AI is revolutionizing industries by enabling machines to perform tasks that once required human intelligence, such as analyzing data, recognizing speech, and automating workflows. However, alongside these benefits come challenges, such as ensuring ethical use, protecting privacy, and addressing job displacement concerns. As technology continues to evolve, it is crucial to strike a balance between harnessing its potential and mitigating its risks to build a more inclusive and sustainable future."
sent = txt.split()

a = Counter(sent)
print(a)