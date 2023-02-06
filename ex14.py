import torch

model = torch.nn.Conv2d(kernel_size=(3, 3), in_channels=8, out_channels=16, stride=(2, 2), bias=True, padding='valid')

pytorch_total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(pytorch_total_params)