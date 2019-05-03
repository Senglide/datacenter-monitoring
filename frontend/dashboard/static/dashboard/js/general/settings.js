var getAverage = false,
    racks = [1, 2, 3],
    s_types = new Map([
        ['temp', 'Temperature (°C)'],
        ['Temperature (°C)', 'temp'],
        ['hum', 'Humidity (%)'],
        ['Humidity (%)', 'hum'],
        ['pduPower', 'Power consumption (W)'],
        ['Power consumption (W)', 'pduPower'],
        ['pduStatus1', 'Top Amperage (A)'],
        ['Top Amperage (A)', 'pduStatus1'],
        ['pduStatus2', 'Bottom Amperage (A)'],
        ['Bottom Amperage (A)', 'pduStatus2'],
        ['pduStatusT', 'Total Amperage (A)'],
        ['Total Amperage (A)', 'pduStatusT']
    ]),
    detailSettingsOptions = new Map([
        ['scope', new Map([
            ['15 Minutes', 900],
            [900, '15 Minutes'],
            ['30 Minutes', 1800],
            [1800, '30 Minutes'],
            ['1 Hour', 3600],
            [3600, '1 Hour'],
            ['2 Hours', 7800],
            [7800, '2 Hours']
        ])],
        ['jump', new Map([
            ['5 Minutes', 300],
            [300, '5 Minutes'],
            ['15 Minutes', 900],
            [900, '15 Minutes'],
            ['30 Minutes', 1800],
            [1800, '30 Minutes'],
            ['1 Hour', 3600],
            [3600, '1 Hour']
        ])],
        ['interval', new Map([
            ['10 Seconds', 10],
            [10, '10 Seconds'],
            ['1 Minute', 60],
            [60, '1 Minute'],
            ['5 Minutes', 300],
            [300, '5 Minutes'],
            ['10 Minutes', 600],
            [600, '10 Minutes']
        ])]
    ]);