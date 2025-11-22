```mermaid
graph TD
subgraph Super-Resolution U-Net
Input(LR Image 512x512) --> Encoder;
Encoder --> E1[Conv + ReLU + Pool]
E1 --> E2[Conv + ReLU + Pool]
E2 --> Bottleneck;
Bottleneck[Residual Blocks] --> D2[Deconv/Upsample];
E2 --> Skip2(Skip Connection)
D2 --> Merge2((Concatenate))
Skip2 --> Merge2
Merge2 --> D1[Deconv/Upsample];
E1 --> Skip1(Skip Connection)
D1 --> Merge1((Concatenate))
Skip1 --> Merge1
Merge1 --> Output_Conv[Final Conv Layer]
Output_Conv --> Output(SR Image 1024x1024)
end

Input --> LossCalc[Loss Calculation]

subgraph Training Objective
LossCalc -- $\mathcal{L}_{Recon}$ + $\lambda \mathcal{L}_{Perc}$ --> Optimizer(Adam Optimizer);
Optimizer --> Encoder;
Optimizer --> Bottleneck;
Optimizer --> D2;
Optimizer --> D1;
HR_GT[HR Ground Truth 1024x1024] --> LossCalc;
end

style Optimizer fill:#b3e0ff, stroke:#333
style LossCalc fill:#ff9999, stroke:#333
