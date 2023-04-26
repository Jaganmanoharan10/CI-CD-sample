# Test Cases for UnitMeasure table
# Count validation on UnitMeasure table
def test_unitmeasure_count_rows(adv_cursor):
    adv_cursor.execute('select count(*) from AdventureWorks2012.Production.UnitMeasure')
    record_count = adv_cursor.fetchval()
    assert record_count == 38


# Primary key column UnitMeasureCode should not contain nulls
def test_not_null(adv_cursor):
    adv_cursor.execute('select  UnitMeasureCode from AdventureWorks2012.Production.UnitMeasure where UnitMeasureCode '
                       'is null')
    unit_measure_code = adv_cursor.fetchall()
    assert len(unit_measure_code) == 0


# Test Cases for Address table
# min max validation on AddressID column in Address table
def test_min_max(adv_cursor):
    adv_cursor.execute('select min(AddressID), max(AddressID) from AdventureWorks2012.Person.Address')
    min_max = adv_cursor.fetchall()
    assert list(min_max[0]) == [1, 32521], "The list not matches the min and max address id"


# Duplicate check on Address table
def test_duplicates(adv_cursor):
    adv_cursor.execute('select AddressID, count(*) from AdventureWorks2012.Person.Address group by AddressID having '
                       'count(*)>1')
    duplicate_records = adv_cursor.fetchall()
    assert len(duplicate_records) == 0, "There are duplicate records"


# Test Cases for Document table
# Validate title in document file name
def test_title_prefixed_filename(adv_cursor):
    title = ''
    file_name = ''
    adv_cursor.execute('select Title, FileName from AdventureWorks2012.Production.Document')
    values = adv_cursor.fetchall()
    for k, v in values:
        title, file_name = k, v
    assert title in file_name, "File name is different to title"


# Validate suffixed file extensions
def test_doc_suffixed_filename(adv_cursor):
    FileName_Ext = ''
    FileExtension = ''
    adv_cursor.execute("select "
                       "SUBSTRING(FileName,CHARINDEX('.', FileName),4) as FileName_EXT, "
                       "FileExtension "
                       "from AdventureWorks2012.Production.Document "
                       "Where SUBSTRING(FileName,CHARINDEX('.', FileName),4) = '.doc'")

    file_extension = adv_cursor.fetchall()
    for x, y in file_extension:
        FileName_Ext, FileExtension = x, y
    assert FileName_Ext == FileExtension, "File extensions are not added properly"
