from plotnine import *


def get_plot(melt_df, x='date', y='value'):
    base_plot = (ggplot(melt_df, aes(x=x, y=y)) +
                 geom_line(size=1) +
                 scale_x_date(date_labels="%Y", date_breaks="6 month") +
                 xlab("Date") +
                 ylab("Value"))
    return base_plot
