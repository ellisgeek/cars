from craigslist import CraigslistForSale
from dotmap import DotMap
import settings

def main():
    filters = {
        'min_price': settings.MIN_PRICE,
        'max_price': settings.MAX_PRICE,
    }

    results = DotMap()

    for site in settings.CRAIGSLIST_SITES:
        temp_results = CraigslistForSale(site=site, category=settings.CRAIGSLIST_CATEGORY, filters=filters).get_results(sort_by='newest', limit=settings.RESULTS_PER_RUN, geotagged=True)
        results[site] = []
        for result in temp_results:
            results[site].append(result)

    results.pprint()


if __name__ == "__main__":
 main()