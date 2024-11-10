install.packages('ggpupr')

# Loading required packages for EDA
pacman::p_load(tidyverse, gt, gtsummary)

df <- read_csv('bioactivity_EDA.csv')

ggplot(data = df)+
  geom_point(aes(x = MW, y = LogP, color = Bioactivity_class, size = pIC50), alpha = .5) +
  scale_color_brewer(palette = 'Paired') +
  scale_size_binned() +
  labs(
    title = "Molecular weight vs. LogP for bioactivity class for Sars-CoV-2 Virus",
    x = "Molecular Weitght (Daltons)",
    y = "LogP",
  color = "Bioactivity Class") +
  theme(plot.title = element_text(face = "bold"),
    axis.title.x = element_text(face = "bold"),
    axis.title.y = element_text(face = "bold")) +
theme_minimal()
