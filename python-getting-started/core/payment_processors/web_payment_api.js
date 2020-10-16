const createNewPaymentRequest = () => {
const pay_resp = new PaymentRequest([{
  supportedMethods: 'secure-payment-confirmation',
  data: {
    action: 'authenticate',
    instrumentId: 'x',
    networkData: Uint8Array.from('x', c => c.charCodeAt(0)),
    timeout: 60000,
    fallbackUrl: 'https://rsolomakhin.github.io/pr/spc/fallback'
  },
}], {
  total: {
    label: 'Total',
    amount: {
      currency: 'USD',
      value: '0.01',
    },
  },
});



	}
