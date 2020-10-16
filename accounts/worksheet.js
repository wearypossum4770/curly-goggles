const company_legal_name = 'Uptown Cabinet Corp.'
const statement_stop_date = new Date('December 31, 2020')

const statement_of_cash_flows = {
    category: {
        'profit': 'prof',
        'depreciation': 'deprec',
        'amortization': 'amortize',
        'impairmentExpense	': 'impair-exp',
        'changeInWorkingCapital': 'work-cap',
        'changeInProvisions': 'chg-provision',
        'interstTax': 'int-tax',
        'tax': 'tax',
    },
}

const calculateAdjustedTrialDebit = () => null
class Worksheet {
    constructor() {
        this.normalDebit = true

        //~ this.normalDebit = normalDebit;
        //~ this.affectsIncome=  affectsIncome;
        //~ this.balanceSheet =balanceSheet;
        //~ this.statementOfCashFlows=statementOfCashFlows;
        //~ this.operatingCashFlow=operatingCashFlow;
    }
    publicMethod() {
        return 'public'
    }
}

class JournalEntry {
    constructor() {
        this.substantiveDocument = null
    }
}
class ReversingEntry {
    constructor() {
        this.isNonReversable = false
        this.isReversable = true
    }
    reversingEntryReducer() {
        /**
         * 1. Use switch statement to determine if isReversable
         * 2. Reverse all accurals
         * 3. DO NOT reverse depreciation or bad debt adjusting entries.
         * 4. Reverse all deferred expense or revenue debits/credits.
         * 5. if !isReversable then break
         * 6. default prompt user
         * */
    }
    testNonReversingEntry() {
        return this.isNonReversable
    }
    testReversingEntry() {
        return this.isReversable
    }
}
const worksheet = {
    title: `${company_legal_name}\nTen-Column Worksheet\nFor the Year Ended ${statement_stop_date.toDateString()}`,
    cash: {
        normalDebit: true,
        isAccrual: false,
        isDeferred: false,
        isReversable: true,
        canReverse: true,
        affectsIncome: false,
        balanceSheet: true,
        statementOfCashFlows: true,
        operatingCashFlow: null,
        trialBalance: {
            dr: 1200,
            cr: 0,
        },
        periodAdjustments: {
            dr: 1200,
            cr: 0,
            re: 123456,
            rec: false,
        },
        adjustedTrialBalance: {
            dr: calculateAdjustedTrialDebit(),
            cr: () => null,
        },
        incomeStatementBalance: {
            dr: () => null,
            cr: () => null,
        },
        balanceSheet: {
            dr: () => null,
            cr: () => null,
        },
    },
}

const newWorksheet = new Worksheet()
const newReversingEntry = new ReversingEntry()
console.log(worksheet.title)

console.log(newReversingEntry.testNonReversingEntry())
console.log(newReversingEntry.testReversingEntry())
console.log(newWorksheet.publicMethod())
