class Fund:
    def __init__(self, fscode: str):
        content = requests.get(self._get_url(fscode))
        jsContent = execjs.compile(content.text)
        self.name = jsContent.eval('fS_name')
        self.code = jsContent.eval('fS_code')
        net_worth_trend = jsContent.eval('Data_netWorthTrend')  # 单位净值走势
        self.date = [self._x2date(day['x']) for day in net_worth_trend]
        self.value = [day['y'] for day in net_worth_trend]

    def __repr__(self):
        return f'name: {self.name}, code: {self.code}'

    def __len__(self):
        return len(self.date)

    def __str__(self):
        return repr(self)

    def _get_url(self, fscode):
        head = 'http://fund.eastmoney.com/pingzhongdata/'  # 东方财富
        tail = '.js?v=' + time.strftime("%Y%m%d%H%M%S", time.localtime())
        return head + fscode + tail

    def _x2date(self, x: int):
        assert isinstance(x, int)
        return datetime.fromtimestamp(x / 1000)

    @property
    def df(self) -> pd.DataFrame:
        return pd.DataFrame({'date': self.date, 'value': self.value})

    def show(self, parent: Optional[Path] = None):
        df = self.df.copy()
        df['delta'] = df.value - df.value.shift(periods=1, fill_value=1.)  # 标签为增量
        df['delta_percent'] = df['delta'] / df.value.shift(periods=1, fill_value=1.) * 100
        df = df.iloc[-240 * 4:]  # 最长展示 4 年
        df.reset_index(drop=True, inplace=True)
        # 插入三根垂直线 周 月 年
        vline_day = [self.date[-i] for i in [240, 20, 5]]  # 除去双休日
        # 插入两根水平线 0.3 0.7
        df.value.quantile([0.3, 0.7])
        hline_value = df.value.quantile([0.3, 0.7]).tolist()
        # 加入标签 每隔 1 个月
        txt_df = df.iloc[::-20]
        txt = {'x': txt_df.date.tolist(), 'y': txt_df.value.tolist(),
               'label': txt_df.apply(lambda row: f'{row["delta_percent"]:.2f}%', axis=1).tolist()}
        base_plot = (ggplot() +
                     geom_line(aes(x='date', y='value'), size=1, color='blue', data=df) +
                     geom_vline(xintercept=vline_day, colour=['red', 'orange', 'green'], size=1, data=df) +
                     geom_hline(yintercept=hline_value, colour=['black', 'pink'], size=2, data=df) +
                     geom_point(aes(x=txt['x'], y=txt['y']), color='red', size=1) +
                     geom_text(aes(label=txt['label'], x=txt['x'], y=txt['y']), color='black', size=14, ha='left', va='top') +  # 从最新到最旧
                     scale_x_date(date_labels="%y-%m", date_breaks="3 month") +
                     xlab("Months") +
                     ylab("Values") +
                     ggtitle(f'{self.name}-{self.code}') +
                     theme(figure_size=(40, 10), text=element_text(family='SimHei'))

                     )
        if parent:
            parent.mkdir(exist_ok=True)
            base_plot.save(parent / f'{self.name}-{self.code}.png', limitsize=False, dpi=250)
        else:
            base_plot.save(parent / f'{self.name}-{self.code}.png', limitsize=False, dpi=250)


    def save(self):
        self.df.to_csv(f'{self.name}-{self.code}.csv')

    def analysis(self):
        df = self.df
        df['delta'] = 0.
        for i, row in df.iterrows():
            if i == 0:
                df.loc[i, 'delta'] = 0
            else:
                df.loc[i, 'delta'] = df.loc[i, 'value'] - df.loc[i - 1, 'value']

        print('星期一到星期五的累计涨幅')
        df['week'] = df['date'].dt.dayofweek + 1
        groups = df.groupby('week')
        for week, group in groups:
            print(week, group['delta'].sum())

        print('年份的累计涨幅')
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        for year, group in df.groupby('year'):
            print(year, group['delta'].sum())

        print('月份的累计涨幅')
        for month, group in df.groupby('month'):
            print(month, group['delta'].sum())