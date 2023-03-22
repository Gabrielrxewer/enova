import torch
import torch.nn as nn

# Define a classe da rede neural
class SimpleDenseNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.layer2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = self.layer2(x)
        return x

# Define os hiperparâmetros
input_size = 10
hidden_size = 20
output_size = 2
learning_rate = 0.001

# Cria uma instância da rede neural
net = SimpleDenseNet(input_size, hidden_size, output_size)

# Define a função de perda e o otimizador
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(), lr=learning_rate)

# Gera dados de entrada e saída aleatórios
inputs = torch.randn(100, input_size)
targets = torch.randint(0, output_size, (100,))

# Loop de treinamento
for epoch in range(100):
    # Forward pass
    outputs = net(inputs)
    loss = criterion(outputs, targets)
    
    # Backward pass e otimização dos parâmetros
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    # Exibe o progresso do treinamento
    if epoch % 10 == 0:
        print(f"Epoch {epoch} - Loss: {loss.item()}")

# Gera novos dados de entrada para fazer previsões
new_inputs = torch.randn(10, input_size)

# Faz previsões usando a rede neural treinada
predicted = net(new_inputs).argmax(dim=1)

