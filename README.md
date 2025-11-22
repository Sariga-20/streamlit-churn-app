```mermaid
graph TD

    subgraph Generator_Training_Loop
        Z_noise[Noise Vector Z] --> G_input_concat
        S_phys_gen[Physics Vector S_phys] --> G_input_concat
        G_input_concat((Concatenate Z and S_phys)) --> G_network[Generator G]

        G_network --> X_fake[Generated Image X_fake]

        X_fake --> D_fake_input_concat
        S_phys_dis_fake[Physics Vector S_phys] --> D_fake_input_concat

        D_fake_input_concat((Concatenate X_fake and S_phys)) --> D_network_gen[Discriminator D]
        D_network_gen --> G_output_prob[D score for fake]
        G_output_prob --> G_loss_calc[Calculate Generator Loss L_G]
        G_loss_calc --> G_network
    end

    subgraph Discriminator_Training_Loop
        X_real[Real Image X_real] --> D_real_input_concat
        S_phys_dis_real[Physics Vector S_phys] --> D_real_input_concat
        D_real_input_concat((Concatenate X_real and S_phys)) --> D_network_real[Discriminator D]
        D_network_real --> D_real_output_prob[D score for real]

        X_fake_from_G[Generated Image X_fake] --> D_fake_input_concat_D
        S_phys_dis_fake_D[Physics Vector S_phys] --> D_fake_input_concat_D
        D_fake_input_concat_D((Concatenate X_fake and S_phys)) --> D_network_fake[Discriminator D]
        D_network_fake --> D_fake_output_prob[D score for fake]

        D_real_output_prob --> D_loss_calc
        D_fake_output_prob --> D_loss_calc

        D_loss_calc[Calculate Discriminator Loss L_D] --> D_network_real
        D_network_real --> D_network_fake
        D_network_fake --> D_network_gen
    end
```



