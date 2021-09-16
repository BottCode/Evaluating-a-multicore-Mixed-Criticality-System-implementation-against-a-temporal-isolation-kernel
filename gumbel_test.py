import matplotlib.pyplot as plt
import numpy as np

criticality_factor = 2
criticality_level = 'HIGH'
low_crit_budget = 1000
period = 70000
hyper_period = 56700000

job_releases = int(hyper_period//period)
JR_budget_exceeding = []

high_crit_budget = low_crit_budget * criticality_factor

mu, beta = (low_crit_budget*0.8, 40) # location and scale
workloads = np.random.gumbel(mu, beta, job_releases)

budget_exceeded = 0

for i in range(0, len(workloads) - 1):
    if workloads[i] >= low_crit_budget:
        print(workloads[i] - low_crit_budget)
        budget_exceeded += 1
        JR_budget_exceeding.append(i)

#print(JR_budget_exceeding)

print(str(budget_exceeded) + "/" + str(len(workloads)) + " = " + str((budget_exceeded/len(workloads))*100) + " %")

count, bins, ignored = plt.hist(workloads, 30, density=True)
plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
         * np.exp( -np.exp( -(bins - mu) /beta) ),
         linewidth=2, color='r')
plt.show()