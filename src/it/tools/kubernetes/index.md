# Kubernetes
Container orchestrator

- Single API to manage everything
- declarative management model
- no more port conflicts
- stateless and stateful application management with data persistence
- effortless management of rollouts and rollbacks


A Kubernetes cluster contains 2 roles:

- `master`: where the Control Manager (CM), scheduler, API Server → cluster management runs
- `workers`: where our containers run, composed of a `kubelet`, `kubeproxy`,`docker runtime`



## ETCD

Database to store cluster status

## Control Manager

Compares the state of the cluster with what is stored in ETCD (application version change, scaling...)

## Scheduler

choose the most appropriate cluster node to run the container (available RAM, CPU, disk space...) → Make the application more resilient

## Kubelet

launches containers (pods), monitors their status...

<!-- ## Kubeproxy -->

## Runtime

Example: Docker Runtime,... → client/server to interact with elements

## Plugins

- network (Container Network Interface)
- storage (Container Storage Interface)
- authentication

## add-ons

DNS server (CoreDNS or kubeDNS)