from sales_analyzer import DataLoader, DataCleaner, SalesAnalyzer, Visualizer, Reporter


def main():
    file_path = "data/raw/sales_data.csv"

    # Load
    loader = DataLoader(file_path)
    df = loader.load()

    # Clean
    cleaner = DataCleaner(df)
    df = cleaner.clean()

    # Analyze
    analyzer = SalesAnalyzer(df)

    print("\n=== BASIC STATISTICS ===")
    stats = analyzer.basic_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")

    print("\n=== TOP PRODUCTS ===")
    print(analyzer.top_products())

    # Visualize
    visualizer = Visualizer(df)
    visualizer.monthly_trend()
    visualizer.category_bar()
    visualizer.sales_distribution()

    # Report
    reporter = Reporter(df)
    reporter.generate()


if __name__ == "__main__":
    main()
