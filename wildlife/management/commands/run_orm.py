from django.core.management.base import BaseCommand
from django.db.models import Count, Sum
from wildlife.models import Property, PropertyType, Province, Organisation, AnnualPopulation, Taxon, User


class Command(BaseCommand):
    help = "Run Wildlife ORM"

    def function_1(self):
        """1. Properties by type"""
        print("1. Properties by type")
        properties = Property.objects.filter(property_type__name__in=["Private", "Community"])
        for prop in properties:
            print(f"- {prop.name} (Type: {prop.property_type.name})")

    def function_2(self):
        """2. Provinces with organisations or properties"""
        print("\n2. Provinces with organisations or properties")
        provinces = Province.objects.filter(
            organisation__isnull=False
        ).union(
            Province.objects.filter(property__isnull=False)
        )
        for province in provinces:
            print(f"- {province.name}")

    def function_3(self):
        """3. Organisation and property count per province"""
        print("\n3. Organisation and property count per province")
        provinces = Province.objects.annotate(
            org_count=Count('organisation'),
            prop_count=Count('property')
        )
        for province in provinces:
            print(f"- {province.name}: {province.org_count} organisations, {province.prop_count} properties")

    def function_4(self):
        """4. Annual population for Acinonyx Jubatus"""
        print("\n4. Annual population for Acinonyx Jubatus")
        population = AnnualPopulation.objects.filter(
            taxon__scientific_name="Acinonyx jubatus",
            year=2021
        ).aggregate(
            total_adult_male=Sum('adult_male'),
            total_adult_female=Sum('adult_female')
        )
        print(f"- Total adult males: {population['total_adult_male']}, Total adult females: {population['total_adult_female']}")

    def function_5(self):
        """5. Species count for 'Zakki Property'"""
        print("\n5. Species count for 'Zakki Property'")
        property_species_count = AnnualPopulation.objects.filter(
            property__name="Zakki Property"
        ).values(
            'taxon'
        ).distinct().count()
        print(f"- Distinct species count: {property_species_count}")

    def function_6(self):
        """6. Organisation with largest area"""
        print("\n6. Organisation with largest area")
        organisation = Organisation.objects.annotate(
                total_area=Sum('property__annualpopulation__area_available_to_species')
        ).order_by('-total_area').first()
        print(f"- Organisation: {organisation.name}, Total Area: {organisation.total_area}")

    def function_7(self):
        """7. Property with most varying species"""
        print("\n7. Property with most varying species")
        property_species = Property.objects.annotate(
            distinct_species=Count('annualpopulation__taxon', distinct=True)
        ).order_by('-distinct_species').first()
        print(f"- Property: {property_species.name}, Distinct Species: {property_species.distinct_species}")

    def function_8(self):
        """8. Property with most animal count"""
        print("\n8. Property with most animal count")
        property_count = Property.objects.annotate(
            total_animals=Sum('annualpopulation__total')
        ).order_by('-total_animals').first()
        print(f"- Property: {property_count.name}, Total Animals: {property_count.total_animals}")

    def function_9(self):
        """9. Province with highest adult male count"""
        print("\n9. Province with highest adult male count")
        province = Province.objects.annotate(
            total_adult_males=Sum('property__annualpopulation__adult_male')
        ).order_by('-total_adult_males').first()
        print(f"- Province: {province.name}, Total Adult Males: {province.total_adult_males}")

    def function_10(self):
        """10. Taxon parent and child taxon"""
        print("\n10. Taxon parent and child taxon")
        taxon_name = "Acinonyx jubatus"  # Example name
        taxon = Taxon.objects.filter(scientific_name=taxon_name).first()
        if taxon:
            print(f"- Taxon: {taxon.scientific_name}")
            if taxon.parent:
                print(f"  Parent Taxon: {taxon.parent.scientific_name}")
            child_taxa = Taxon.objects.filter(parent=taxon)
            if child_taxa.exists():
                print(f"  Child Taxa:")
                for child in child_taxa:
                    print(f"    - {child.scientific_name}")
            else:
                print("  No Child Taxa")
        else:
            print("- Taxon not found")

    def function_11(self):
        """11. Taxa without children"""
        print("\n11. Taxa without children")
        taxa = Taxon.objects.filter(parent__isnull=True)
        for taxon in taxa:
            print(f"- {taxon.scientific_name}")

    def function_12(self):
        """12. Top user by annual population records"""
        print("\n12. Top user by annual population records")
        user = User.objects.annotate(
            record_count=Count('annualpopulation')
        ).order_by('-record_count').first()
        print(f"- User: {user.username}, Total Records: {user.record_count}")

    def handle(self, *args, **options):
        """Logic of the command"""
        self.function_1()
        self.function_2()
        self.function_3()
        self.function_4()
        self.function_5()
        self.function_6()
        self.function_7()
        self.function_8()
        self.function_9()
        self.function_10()
        self.function_11()
        self.function_12()
