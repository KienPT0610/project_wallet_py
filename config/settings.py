API_URL = "https://data-seed-prebsc-1-s1.binance.org:8545/"
CONTRACT_ADDRESS = "0x20492C8255b075F73906b2849118dB1A2C4b3f01"
CONTRACT_ABI = [
    { "inputs": [], "stateMutability": "nonpayable", "type": "constructor" },
    {
      "inputs": [
        { "internalType": "address", "name": "spender", "type": "address" },
        { "internalType": "uint256", "name": "allowance", "type": "uint256" },
        { "internalType": "uint256", "name": "needed", "type": "uint256" }
      ],
      "name": "ERC20InsufficientAllowance",
      "type": "error"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "sender", "type": "address" },
        { "internalType": "uint256", "name": "balance", "type": "uint256" },
        { "internalType": "uint256", "name": "needed", "type": "uint256" }
      ],
      "name": "ERC20InsufficientBalance",
      "type": "error"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "approver", "type": "address" }
      ],
      "name": "ERC20InvalidApprover",
      "type": "error"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "receiver", "type": "address" }
      ],
      "name": "ERC20InvalidReceiver",
      "type": "error"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "sender", "type": "address" }
      ],
      "name": "ERC20InvalidSender",
      "type": "error"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "spender", "type": "address" }
      ],
      "name": "ERC20InvalidSpender",
      "type": "error"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "Approval",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "Transfer",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "string",
          "name": "content",
          "type": "string"
        }
      ],
      "name": "TransferToken",
      "type": "event"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "owner", "type": "address" },
        { "internalType": "address", "name": "spender", "type": "address" }
      ],
      "name": "allowance",
      "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "spender", "type": "address" },
        { "internalType": "uint256", "name": "value", "type": "uint256" }
      ],
      "name": "approve",
      "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "account", "type": "address" }
      ],
      "name": "balanceOf",
      "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "from", "type": "address" },
        { "internalType": "uint256", "name": "amount", "type": "uint256" }
      ],
      "name": "burn",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "decimals",
      "outputs": [{ "internalType": "uint8", "name": "", "type": "uint8" }],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "user", "type": "address" }
      ],
      "name": "getReceiveTransactions",
      "outputs": [
        {
          "components": [
            { "internalType": "uint256", "name": "id", "type": "uint256" },
            { "internalType": "address", "name": "from", "type": "address" },
            { "internalType": "address", "name": "to", "type": "address" },
            { "internalType": "uint256", "name": "amount", "type": "uint256" },
            { "internalType": "string", "name": "content", "type": "string" }
          ],
          "internalType": "struct WalletToken.Transaction[]",
          "name": "",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "user", "type": "address" }
      ],
      "name": "getSendTransactions",
      "outputs": [
        {
          "components": [
            { "internalType": "uint256", "name": "id", "type": "uint256" },
            { "internalType": "address", "name": "from", "type": "address" },
            { "internalType": "address", "name": "to", "type": "address" },
            { "internalType": "uint256", "name": "amount", "type": "uint256" },
            { "internalType": "string", "name": "content", "type": "string" }
          ],
          "internalType": "struct WalletToken.Transaction[]",
          "name": "",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "to", "type": "address" },
        { "internalType": "uint256", "name": "amount", "type": "uint256" }
      ],
      "name": "mint",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "name",
      "outputs": [{ "internalType": "string", "name": "", "type": "string" }],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "", "type": "address" },
        { "internalType": "uint256", "name": "", "type": "uint256" }
      ],
      "name": "receiveTransactions",
      "outputs": [
        { "internalType": "uint256", "name": "id", "type": "uint256" },
        { "internalType": "address", "name": "from", "type": "address" },
        { "internalType": "address", "name": "to", "type": "address" },
        { "internalType": "uint256", "name": "amount", "type": "uint256" },
        { "internalType": "string", "name": "content", "type": "string" }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "to", "type": "address" },
        { "internalType": "uint256", "name": "amount", "type": "uint256" },
        { "internalType": "string", "name": "content", "type": "string" }
      ],
      "name": "sendToken",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "", "type": "address" },
        { "internalType": "uint256", "name": "", "type": "uint256" }
      ],
      "name": "sendTransactions",
      "outputs": [
        { "internalType": "uint256", "name": "id", "type": "uint256" },
        { "internalType": "address", "name": "from", "type": "address" },
        { "internalType": "address", "name": "to", "type": "address" },
        { "internalType": "uint256", "name": "amount", "type": "uint256" },
        { "internalType": "string", "name": "content", "type": "string" }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "symbol",
      "outputs": [{ "internalType": "string", "name": "", "type": "string" }],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "totalSupply",
      "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "to", "type": "address" },
        { "internalType": "uint256", "name": "value", "type": "uint256" }
      ],
      "name": "transfer",
      "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        { "internalType": "address", "name": "from", "type": "address" },
        { "internalType": "address", "name": "to", "type": "address" },
        { "internalType": "uint256", "name": "value", "type": "uint256" }
      ],
      "name": "transferFrom",
      "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
      "stateMutability": "nonpayable",
      "type": "function"
    }
]