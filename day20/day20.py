import math
import heapq
from abc import ABC, abstractmethod

class Module(ABC):
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs

    @abstractmethod
    def recieve_pulse(input, pulse):
        pass

class Broadcaster(Module):
    def recieve_pulse(self, pulse):
        return 0

class FlipFlop(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.state = 0
    
    def recieve_pulse(self, input, pulse):
        if pulse:
            return
        else:
            self.state = not self.state
            return self.state

class Conjunction(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)

    def set_memory(self, modules):
        memory = {}
        for name, module in modules.items():
            if self.name in module.outputs:
                memory[name] = 0

        self.memory = memory
    
    def recieve_pulse(self, input, pulse):
        self.memory[input] = pulse
        
        if all(self.memory.values()):
            return 0
        else:
            return 1

if __name__ == "__main__":
    with open("day20.txt", "r") as f:
        module_config = {}
        for module in f.read().split("\n"):
            module_def, outputs = module.split(" -> ")
            outputs = outputs.split(", ")
            if module_def == "broadcaster":
                module_config[module_def] = Broadcaster(module_def, outputs)
            else:
                module_type, name = module_def[0], module_def[1:]
                if module_type == "%": 
                    module_config[name] = FlipFlop(name, outputs)
                elif module_type == "&": 
                    module_config[name] = Conjunction(name, outputs)

    for name, module in module_config.items():
        if type(module) == Conjunction:
            module.set_memory(module_config)

    low_count, high_count = 0, 0
    for i in range(5000):
        if i == 1000:
            print(f"Part 1; {low_count * high_count}")
            
        low_count += 1
        queue = [("broadcaster", 0)]
        while queue:
            module, pulse = heapq.heappop(queue)
                
            for output in module_config[module].outputs:
                if pulse: high_count += 1
                else: low_count += 1
                
                if output in module_config:
                    next_pulse = module_config[output].recieve_pulse(module, pulse)
                    if next_pulse is not None:
                        heapq.heappush(queue, (output, next_pulse))
    
                        if output == "dl" and next_pulse == 1: dl = i+1
                        elif output == "vk" and next_pulse == 1: vk = i+1
                        elif output == "pm" and next_pulse == 1: pm = i+1
                        elif output == "ks" and next_pulse == 1: ks = i+1
                            
    print(f"Part 2: {math.lcm(*[dl, vk, pm, ks])}")