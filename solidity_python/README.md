

    - pip install eth-brownie
    - create folder for the bank or app name
        - mkdir DEFI
        - cd  DEFI
        - brownie init
            - Folders
                - Build: where all json and contract ABI will reside once the contract is deployed to the block chain.
                - contracts: where we will be writing our contracts with solidity files.
                - interfaces: where we will keep all interfaces if we will use any
                - reports:
                - scripts: Is where we will be writing the deployment scripts or to interact with our smart contracts.
                - tests: if we will write any test cases, it goes here.
        
        - touch DEFI/contracts/DefiBank.sol
        - cd into DEFI file
            - create and edit 'touch brownie-config.yaml'
            - run 'brownie compile' to compile the project

        - After writting the issueInterest
            - run "brownie compile"
            - write a script to deploy
                - make a file in scripts 'deploy.py'
                - then edit the file as follows
                - install dotenv package to get env variables
                    - run "pip install python-dotenv"
                    - get your private key from metamask or ganash
                    - create an account with infura and create new project(infura.io)
                - now deploy project using infura 
                    - brownie run scripts/deploy.py --network rinkeby
                    - confirm by copying the address 
                        - visit (rinkeby.etherscan.io)
                - Interact with the deployed contracts
                    - create "scripts/interact.py"
                    - now edit as follow "check scripts/interact.py"
                    
                    - NOTE: YOU CAN FIND ALL ADDRESS IN "build/deployments/map.json". The first one is the latest one.

                    - run "brownie run scripts/interact.py --network rinkeby"
        - Install frontend (e.g flask)
            - run "pip install flask"
            - run "pip install Flask-WTF"
            - create "frontend/run.py"
            - edit as follows
            - create two folders
                - run "mkdir frontend/templates frontend/static"
                    - templates: keep our html files
                    - static: keep our css files
                - create "touch frontend/templates/base.html"
                - create "touch frontend/templates/index.html"

                