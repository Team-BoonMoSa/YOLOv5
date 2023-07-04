import torch
import torch.neuron


if __name__ == "__main__":
    weights = 'best.pt'
    device = torch.device('cpu')

    model = torch.hub.load('./',
                           'custom',
                           path='best.pt',
                           source='local',
                           force_reload=True)

    input_tensor = torch.randn(1, 3, 640, 640, dtype=torch.float32)
    print(input_tensor.shape, input_tensor.dtype)
    model.eval()
    print(model(input_tensor))

    convert_neuron = True
    if convert_neuron:
        model_neuron = torch.neuron.trace(model, [input_tensor])
        filename = 'model_neuron.pt'
        model_neuron.save(filename)