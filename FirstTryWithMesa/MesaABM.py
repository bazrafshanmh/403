import networkx as nx
from mesa import Agent, Model
from mesa.space import NetworkGrid
from mesa.datacollection import DataCollector
import matplotlib.pyplot as plt


class RumorAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = "ignorant"
    
    def step(self):
        if self.state == "spreader":
            neighbors = self.model.grid.get_neighbors(self.unique_id, include_center=False)
            for neighbor in neighbors:
                agent = self.model.grid.get_cell_list_contents([neighbor])[0]
                if agent.state == "ignorant" and self.random.random() < self.model.spread_prob:
                    agent.state = "spreader"
                if self.random.random() < self.model.stop_prob:
                    self.state = "stifler"

class RumorModel(Model):
    def __init__(self, gexf_file, spread_prob, stop_prob, numberOfFirstSpreaders):
        self.spread_prob = spread_prob
        self.stop_prob = stop_prob
        self.graph = nx.read_gexf(gexf_file)
        self.grid = NetworkGrid(self.graph)
        self.numberOfFirstSpreaders = numberOfFirstSpreaders
        self.agents = []
        for i, node in enumerate(self.graph.nodes):
            agent = RumorAgent(i, self)
            self.grid.place_agent(agent, node)
            self.agents.append(agent)


        first_agents = self.random.choices(self.agents, k=self.numberOfFirstSpreaders )
        for agent in first_agents:
            agent.state = "spreader"
        
        self.datacollector = DataCollector(
            {"Ignorant": lambda m: self.count_state(m, "ignorant"),
             "Spreader": lambda m: self.count_state(m, "spreader"),
             "Stifler": lambda m: self.count_state(m, "stifler")}
        )
    def step(self):
        self.datacollector.collect(self)
        for agent in self.agents:
            agent.step()
    @staticmethod
    def count_state(model, state):
        return sum(1 for agent in model.agents if agent.state == state)

model = RumorModel(gexf_file="./Graph.gexf", spread_prob=0.1, stop_prob=0.05, numberOfFirstSpreaders=1)

# اجرای 50 گام زمانی
for i in range(50):
    model.step()

# رسم نتایج
data = model.datacollector.get_model_vars_dataframe()
data.plot()
plt.xlabel("Time Steps")
plt.ylabel("Number of Agents")
plt.title("Rumor Spread Dynamics")
plt.show()