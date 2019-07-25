from setuptools import find_packages, setup


setup(
    name="water_contamination",
    version="1.0.0",
    description="Water_Contamination Analysis",
    author="Isaiah Brant",
    author_email="brant2302@gmail.com",
    url="https://github.com/ibrant02/water-contamination",
    zip_safe=False,
    install_requires=[
        'biopython==1.72',
        'numpy==1.15.4',
    ],
    entry_points={'console_scripts':['find_contaminants=water_contamination.scripts.run:main']}
)
